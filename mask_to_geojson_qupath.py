import numpy as np
import json
from pathlib import Path
from skimage import measure


def masks_to_geojson(mask_path, output_path=None, classification_name="Cell Nuclei"):
    """
    Convert instance segmentation mask (.npy) to GeoJSON format for QuPath.
    
    Args:
        mask_path: Path to .npy file containing instance segmentation mask
        output_path: Path to save GeoJSON file (default: same as mask_path with .geojson extension)
        classification_name: Name for the classification in QuPath (default: "Cell")
    
    Returns:
        dict: GeoJSON FeatureCollection
    """
    # Load the mask
    masks = np.load(mask_path)
    
    # Get unique instance IDs (excluding background 0)
    unique_labels = np.unique(masks)
    unique_labels = unique_labels[unique_labels != 0]
    
    # Initialize FeatureCollection
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    
    # Process each instance
    for label_id in unique_labels:
        # Create binary mask for this instance
        binary_mask = (masks == label_id).astype(np.uint8)
        
        # Find contours using skimage (more robust than cv2 for complex shapes)
        contours = measure.find_contours(binary_mask, 0.5)
        
        # Filter out empty contours and ensure minimum points (at least 3 for a valid polygon)
        valid_contours = []
        for contour in contours:
            if len(contour) >= 3:  # Minimum 3 points for a polygon
                # Convert from (row, col) to (x, y) coordinates
                # Note: QuPath uses (x, y) where x is column and y is row
                coords = [[float(col), float(row)] for row, col in contour]
                
                # Close the polygon if not already closed
                if coords[0] != coords[-1]:
                    coords.append(coords[0])
                
                valid_contours.append(coords)
        
        # Skip this instance if no valid contours found
        if len(valid_contours) == 0:
            print(f"Warning: Instance {label_id} has no valid contours, skipping...")
            continue
        
        # Determine geometry type based on number of contours
        if len(valid_contours) == 1:
            # Single polygon - use Polygon type
            geometry = {
                "type": "Polygon",
                "coordinates": [valid_contours[0]]  # Polygon format: [[coords]]
            }
        else:
            # Multiple polygons - use MultiPolygon type
            # MultiPolygon format: [[[coords1]], [[coords2]], ...]
            geometry = {
                "type": "MultiPolygon",
                "coordinates": [[coords] for coords in valid_contours]
            }
        
        # Create feature for this instance
        feature = {
            "type": "Feature",
            "id": f"nuclei_{int(label_id)}",
            "geometry": geometry,
            "properties": {
                "objectType": "annotation",
                "classification": {
                    "name": classification_name,
                    "color": [200, 0, 0]  # RGB color (red by default)
                },
                "isLocked": False
            }
        }
        
        geojson["features"].append(feature)
    
    # Save to file
    if output_path is None:
        output_path = Path(mask_path).with_suffix('.geojson')
    else:
        output_path = Path(output_path)
    
    with open(output_path, 'w') as f:
        json.dump(geojson, f, indent=2)
    
    print(f"Saved {len(geojson['features'])} instances to {output_path}")
    return geojson


# Batch processing function
def batch_masks_to_geojson(mask_dir, output_dir=None, pattern="*_contours.npy"):
    """
    Convert all mask files in a directory to GeoJSON.
    
    Args:
        mask_dir: Directory containing .npy mask files
        output_dir: Directory to save GeoJSON files (default: same as mask_dir)
        pattern: Glob pattern to match mask files
    """
    mask_dir = Path(mask_dir)
    if output_dir is None:
        output_dir = mask_dir
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    mask_files = list(mask_dir.glob(pattern))
    print(f"Found {len(mask_files)} mask files")
    
    for mask_file in mask_files:
        output_file = output_dir / mask_file.with_suffix('.geojson').name
        masks_to_geojson(mask_file, output_file)


if __name__ == "__main__":

    # path to mask predictions. e.g.,
    mask_path = 'stage3_paper/cellpose-sam-inference-gpu/result/2-WXA-FFS-PH-20220322-01(2) rat kindey PAS_patch_5120_47616_contours.npy'
    masks_to_geojson(mask_path=mask_path) # default to same location as mask_path

    # Drag the image, and then geojson mask to Qupath for further Human-in-the-loop correction