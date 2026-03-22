"""
Visualize a CellViT instance segmentation .npy mask as a color-coded PNG.

Usage:
    python visualize_instance_mask.py --input /path/to/mask_contours.npy
    python visualize_instance_mask.py --input /path/to/mask_contours.npy --output /path/to/output.png
"""

import argparse
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def visualize(npy_path: str, out_path: str) -> None:
    mask = np.load(npy_path).astype(np.int32)
    n_instances = int(mask.max())

    np.random.seed(42)
    colors = np.random.randint(50, 255, size=(n_instances + 1, 3), dtype=np.uint8)
    colors[0] = [0, 0, 0]  # background = black

    rgb = colors[mask]

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.imshow(rgb)
    ax.set_title(f"Instance Segmentation — {n_instances} cells", fontsize=13)
    ax.axis("off")
    fig.savefig(out_path, bbox_inches="tight", dpi=150, pad_inches=0.1)
    plt.close()
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize instance segmentation .npy mask")
    parser.add_argument("--input", type=str, required=True, help="Path to _contours.npy file")
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output PNG path (default: same location as input, suffix _vis.png)",
    )
    args = parser.parse_args()

    out = args.output
    if out is None:
        out = args.input.replace("_contours.npy", "_instance_seg.png")
        if out == args.input:
            out = os.path.splitext(args.input)[0] + "_instance_seg.png"

    visualize(args.input, out)
