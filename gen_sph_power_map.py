import sys, argparse
import numpy as np
import csv
from distance import SphericalAmbisonicsVisualizer, SphericalSourceVisualizer
from audio import load_wav
from video import VideoWriter
from matplotlib import pyplot as plt


def run(input_fn, output_fn, position_fn='', angular_res='', csv_output='frame_data.csv'):
    
    data, rate = load_wav(input_fn)
    print(f' The sample rate of the WAV file is {rate}. You should set (rs*window) + 1 for Mel spectogram')
    duration = data.shape[0] / float(rate)

    ambiVis = SphericalAmbisonicsVisualizer(data, rate, angular_res=angular_res)
    if position_fn:
        srcVis = SphericalSourceVisualizer(position_fn, duration, ambiVis.visualization_rate(), angular_res=angular_res)

    writer = VideoWriter(output_fn, video_fps=ambiVis.visualization_rate(), overwrite=True)

    cmap = np.stack(plt.get_cmap('inferno').colors)
    
    with open(csv_output, 'w', newline='') as csvfile:
        
        csvwriter = csv.writer(csvfile)
        header = ['Pixel_' + str(i) for i in range(1, 19 * 36 + 1)]
        csvwriter.writerow(header)
        
        while True:
            frame = ambiVis.get_next_frame()
            if frame is None:
                break
            
            frame /= frame.max()

            if position_fn:
                frame += srcVis.get_next_frame()

            # Normalize and apply colormap for video visualization
            frame_video = ((frame / frame.max()) * 255).astype(np.uint8)
            frame_video = (cmap[frame_video] * 255).astype(np.uint8)
            writer.write_frame(frame_video)

            # Flatten the frame to write into CSV
            frame_flattened = frame.flatten()
            csvwriter.writerow(frame_flattened)


def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('input_fn',    help='Input ambisonics filename.')
    parser.add_argument('output_fn',   help='Output video filename to store spherical power map.')
    parser.add_argument('--position_fn', default='', help='Ground-truth position file. Source locations will be superimposed.')
    parser.add_argument('--angular_res', default=10., type=float, help='Angular resolution.')
    return parser.parse_args(sys.argv[1:])


if __name__ == '__main__':
    args = parse_arguments()
    run(**vars(args))