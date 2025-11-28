# StarDist Extension Setup for QuPath

This guide explains how to install the **StarDist extension** in **QuPath**, load a pretrained model, and run nucleus detection on whole-slide images or patches.

---

## 1. Install QuPath
Download and install **QuPath v0.5.0** (I installed):  
https://qupath.github.io

---

## 2. Install the StarDist Extension

1. If using QuPath v 0.5.0; the qupath-extension-stardist-0.5.0.jar is already downloaded and saved.

If using other version:
    Open the StarDist extension GitHub releases page:  
   https://github.com/qupath/qupath-extension-stardist/releases  
     Download the appropriate `.jar` file  

2.Drag the `.jar` file into QuPath.  

3. Verify installation in QuPath:  


---

## 3. Download a StarDist Model (.pb)
Official models are available here:  
https://github.com/qupath/models/tree/main/stardist

We use:  
- **H&E / PAS nuclei:** `he_heavy_augment.pb`

Save the `.pb` file somewhere accessible.

---

## 4. Prepare Your Image
Drag a **WSI** or **image patch** into QuPath.

---

## 5. Run StarDist Nucleus Detection in QuPath
1. Go to:  
   **`Extensions` → `StarDist` → `StarDist H&E nucleus detection script`**
   
2. In the Script Editor, set the model path:

```groovy
def modelPath = '/path/to/model.pb'
```
This script is the same as `qupath-stardist-detect.groovy`

1. Adjust parameters if needed (optional).  
2. Draw or select a Rectangle region on the image in QuPath.  
3. Press **Run**.

## 6. Use our own models

Change the path in groovy script
```groovy
def modelPath = '/path/to/our/model.pb'
```
---
## 7. Flexible Detection-Annotations groovy script

The original groovy script will generate **Detections**

We provide the `qupath-stardist-detect-annotate.groovy`, which will make the run outputs as **QuPath Annotations** for easy correct.

## 6. Documentation
More details and parameter descriptions:  
https://qupath.readthedocs.io/en/0.5/docs/deep/stardist.html
