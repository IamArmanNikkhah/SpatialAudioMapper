# SpatialAudioMapper

**Toolkit for mapping, analyzing, and visualizing spatial audio signals.**

SpatialAudioMapper provides a set of Python scripts for processing multichannel audio recordings and generating spatial representations such as spherical power maps. It includes utilities for estimating the direction of arrival of sounds, computing distance cues, and projecting audio intensity onto spherical or planar displays. The goal is to facilitate research in spatial audio, virtual acoustics, and immersive media.

## Features

- **Generate spherical power maps:** Compute spherical power maps from multichannel audio files to visualize the distribution of acoustic energy in 3D space.
- **Position estimation:** Estimate the azimuth and elevation of sound sources using time‑difference of arrival and amplitude cues.
- **Audio & video decoders:** Scripts to decode and preprocess audio (`audio.py`) and video (`video.py`) streams for spatial analysis.
- **Distance calculations:** Functions to compute distances between sources and sensors (`distance.py`) and convert between coordinate systems.
- **Command‑line interface:** Simple command‑line tools (`cmd.py`, `gen_sph_power_map.py`) for running analyses without writing additional code.
- **Sample data:** Includes example data in `Sample Spatial Audio/` to test the pipeline and visualize results.

## Repository Structure

```
SpatialAudioMapper/
├── Sample Spatial Audio/    # Sample audio files for testing
├── audio.py                 # Audio decoding and preprocessing
├── cmd.py                   # Command‑line interface
├── common.py                # Shared helper functions
├── decoder.py               # Decoder for specific audio formats
├── distance.py              # Functions for distance and geometry calculations
├── gen_sph_power_map.py     # Generate spherical power maps from audio
├── ioilib_position.py       # I/O utilities for position data
├── position.py              # Source position estimation utilities
└── video.py                 # Video processing for audiovisual datasets
```

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/IamArmanNikkhah/SpatialAudioMapper.git
   cd SpatialAudioMapper
   ```

2. **Install dependencies** (Python 3.7+ recommended):

   ```bash
   pip install numpy scipy matplotlib soundfile librosa opencv-python
   ```

   Adjust the dependencies as needed based on your environment and the scripts you plan to run.

3. **Generate a spherical power map**:

   ```bash
   # Example: compute a power map for a multichannel WAV file
   python gen_sph_power_map.py --input Sample\ Spatial\ Audio/sample_audio.wav --output output_map.png
   ```

   This will process the input audio and save a visualization of the spatial power distribution. Use `--help` to see all available options.

4. **Estimate source positions**:

   ```bash
   python position.py --input Sample\ Spatial\ Audio/sample_audio.wav
   ```

   This script outputs estimated azimuth and elevation angles for dominant sound sources.

## Contributing

Contributions are welcome! If you have suggestions for new features, bug fixes, or improvements, please open an issue or submit a pull request.

1. Fork the repository and create your feature branch:

   ```bash
   git checkout -b feature/MyFeature
   ```

2. Commit your changes and push the branch:

   ```bash
   git commit -am "Add MyFeature"
   git push origin feature/MyFeature
   ```

3. Open a pull request describing your changes.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it for research or educational purposes.
