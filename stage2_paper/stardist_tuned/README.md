# StarDist (Histo.) Fine-tuning and Models

## Requirements

- Python 3.8 and TensorFlow 2.4.4 (the version we use)
- CUDA-compatible GPU (recommended) or CPU
- NVIDIA GPU drivers (for GPU support)

## Installation 

If already created the conda environment and installed packages for stardist inference following the [Step-by-Step Install instructions (option 1)](../../stage1_paper/stardist-inference-gpu/README.md#option-1-step-by-step-install), then only need to install `gputools` for training acceleration.
```bash
pip install gputools==0.2.14
```