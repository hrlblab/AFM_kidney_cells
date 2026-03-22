#!/usr/bin/env python3
"""
Debug script to inspect model structure and checkpoint contents
"""

import torch
import sys
import os

# Add the parent directory to the path
currentdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, currentdir)

from models.segmentation.cell_segmentation.cellvit_virchow import CellViTVirchow
from utils.tools import unflatten_dict

def inspect_checkpoint(checkpoint_path):
    """Inspect the contents of a checkpoint file"""
    print(f"=== Inspecting checkpoint: {checkpoint_path} ===")
    
    checkpoint = torch.load(checkpoint_path, map_location="cpu")
    
    print(f"Checkpoint keys: {list(checkpoint.keys())}")
    
    if "arch" in checkpoint:
        print(f"Model architecture: {checkpoint['arch']}")
    
    if "model_state_dict" in checkpoint:
        state_dict = checkpoint["model_state_dict"]
        print(f"State dict keys (first 10): {list(state_dict.keys())[:10]}")
        print(f"Total state dict keys: {len(state_dict.keys())}")
        
        # Show some example keys
        for i, key in enumerate(list(state_dict.keys())[:20]):
            print(f"  {i+1:2d}. {key} -> {state_dict[key].shape}")
    
    if "config" in checkpoint:
        config = unflatten_dict(checkpoint["config"], ".")
        print(f"Config keys: {list(config.keys())}")
        if "data" in config:
            print(f"Data config: {config['data']}")
        if "model" in config:
            print(f"Model config: {config['model']}")

def inspect_model_structure(model):
    """Inspect the structure of a model"""
    print(f"\n=== Inspecting model structure ===")
    print(f"Model type: {type(model).__name__}")
    
    print(f"\n--- Named modules ---")
    for name, module in model.named_modules():
        if len(list(module.children())) == 0:  # Only leaf modules
            print(f"  {name} -> {type(module).__name__}")
    
    print(f"\n--- Named parameters ---")
    for name, param in model.named_parameters():
        print(f"  {name} -> {param.shape}")
    
    print(f"\n--- State dict keys ---")
    state_dict = model.state_dict()
    print(f"Total parameters: {len(state_dict.keys())}")
    for i, key in enumerate(list(state_dict.keys())[:20]):
        print(f"  {i+1:2d}. {key} -> {state_dict[key].shape}")

def compare_checkpoint_and_model(checkpoint_path, model):
    """Compare checkpoint keys with model keys"""
    print(f"\n=== Comparing checkpoint and model ===")
    
    checkpoint = torch.load(checkpoint_path, map_location="cpu")
    checkpoint_keys = set(checkpoint["model_state_dict"].keys())
    model_keys = set(model.state_dict().keys())
    
    missing_in_model = checkpoint_keys - model_keys
    missing_in_checkpoint = model_keys - checkpoint_keys
    
    print(f"Keys in checkpoint but missing in model: {len(missing_in_model)}")
    if missing_in_model:
        for key in list(missing_in_model)[:10]:
            print(f"  - {key}")
        if len(missing_in_model) > 10:
            print(f"  ... and {len(missing_in_model) - 10} more")
    
    print(f"Keys in model but missing in checkpoint: {len(missing_in_checkpoint)}")
    if missing_in_checkpoint:
        for key in list(missing_in_checkpoint)[:10]:
            print(f"  - {key}")
        if len(missing_in_checkpoint) > 10:
            print(f"  ... and {len(missing_in_checkpoint) - 10} more")

def main():
    # Example usage
    checkpoint_path = "/home/guoj5/Documents/cellvit-clean/cellvit++(checkpoints)/CellViT-Virchow-x40-AMP.pth"
    
    if not os.path.exists(checkpoint_path):
        print(f"Checkpoint not found: {checkpoint_path}")
        return
    
    # Inspect checkpoint
    inspect_checkpoint(checkpoint_path)
    
    # Load checkpoint to get config
    checkpoint = torch.load(checkpoint_path, map_location="cpu")
    config = unflatten_dict(checkpoint["config"], ".")
    
    # Create model
    model = CellViTVirchow(
        model_virchow_path=None,  # Don't load during construction
        num_nuclei_classes=config["data"]["num_nuclei_classes"],
        num_tissue_classes=config["data"]["num_tissue_classes"],
    )
    
    # Inspect model
    inspect_model_structure(model)
    
    # Compare
    compare_checkpoint_and_model(checkpoint_path, model)

if __name__ == "__main__":
    main() 