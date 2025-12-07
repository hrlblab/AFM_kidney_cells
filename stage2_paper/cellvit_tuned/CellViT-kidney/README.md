
# CellViT Experiments

## Inference Script
(image patch size of 512 by 512)
```bash
python /path/to/cell_segmentation/inference/inference_cellvit_experiment_kidney.py \
    --gpu 0 \
    --model /path/to/pretrained_checkpoint \
    --patching True \
    --overlap 0 \
    --datasets_dir /path/to/png_folder \
    --outputs_dir /path/to/output_folder
```
or running the bash script at: 
https://github.com/junlinguo/CellViT-Kidney/blob/main/bash/inference_run.sh



The cellvit pretrained checkpoint from CellViT paper can be found: 
- [CellViT-SAM-H](https://drive.google.com/uc?export=download&id=1MvRKNzDW2eHbQb5rAgTEp6s2zAXHixRV) 🚀
- [CellViT-256](https://drive.google.com/uc?export=download&id=1tVYAapUo1Xt8QgCN22Ne1urbbCZkah8q) (The one used in this repo)
- [CellViT-SAM-H-x20](https://drive.google.com/uc?export=download&id=1wP4WhHLNwyJv97AK42pWK8kPoWlrqi30)
- [CellViT-256-x20](https://drive.google.com/uc?export=download&id=1w99U4sxDQgOSuiHMyvS_NYBiz6ozolN2)

  
## Reference
- CellViT paper: [link](https://arxiv.org/abs/2306.15350)
- CellViT github: this forked repo or [link](https://github.com/TIO-IKIM/CellViT)
- This repo is based on the paper: [Assessment of Cell Nuclei AI Foundation Models in Kidney Pathology](https://arxiv.org/abs/2408.06381)

## Paper Experiment: Finetune CellViT256 on PanNuke Dataset 

**Objective:**  
- Nuclei instance segmentation
- Nuclei classification
- Tissue classification

**Command to run:**
```bash
python /path/to/cellvit/CellViT-kidney/cell_segmentation/run_cellvit.py --gpu 0 --config /home/guoj5/Desktop/cellvit/CellViT-kidney/configs/examples/cell_segmentation/train_cellvit_copy.yaml
```

# Flexible Training Experiments (Optional)
- Nuclei instance segmentation only

**Data:**  

instance-segmentation data.  
Data preparation (as PanNuke dataset file structures, currently) follows: `/mnt/Data/guoj5/fintuned_dummy/instructions.txt`
(or `./dataset_instructions.txt`)

**Main script for training experiment:**  

`/path/to/CellViT-kidney/cell_segmentation/run_cellvit_mod.py`

**Experiments Configuration [Important!!!]:**  

`/path/to/CellViT-kidney/configs/examples/cell_segmentation/my_experiment_logs/train_cellvit/xxx.yaml`

The experiments are also logged by Weights and Biases.

**Local run of training bash script example:**

```bash
python /path/to/run_cellvit_mod.py \ 
        --gpu 0 \
        --config /path/to/CellViT-kidney/configs/examples/cell_segmentation/my_experiment_logs/train_cellvit/train_fold0_all.yaml
```

## Evaluate 
```bash
python /path/to/cell_segmentation/evaluate.py \
        --predictions /path/to/the/prediction/folder \
        --gt /path/to/the/groundth/folder  \
        --log_csv[optional] /path/to/save/metric/csv

```

## Bash script running experiments above 

`./bash/xxx_run.sh`

## Appendix: Notes for the code modification to allowing training the CellViT model without tissue classification information, etc

### Customize 'experiment_cellvit_instance.py' to finetune pretrained model 
- [Loss functiuons: Disable nuclei type classification and tissue classification objectives](https://github.com/junlinguo/CellViT-Kidney/blob/main/cell_segmentation/experiments/experiment_cellvit_instance.py#L392-L420)
- [Get transforms: Reshape/Crop image to (256, 256) to continue finetuning the pretrained model](https://github.com/junlinguo/CellViT-Kidney/blob/main/cell_segmentation/experiments/experiment_cellvit_instance.py#L729)
- Dataloader: drop_last = True
- [select_dataset: adding 'PanNukeDataset_mod'](https://github.com/junlinguo/CellViT-Kidney/blob/main/cell_segmentation/experiments/experiment_cellvit_instance.py#L530-L536)


### Customize 'cell_segmentation/datasets/pannuke_like_instance.py' [class PanNukeDataset_mod]
- [nuclei/tissue types information: disabled](https://github.com/junlinguo/CellViT-Kidney/blob/main/cell_segmentation/datasets/pannuke_like_instance.py#L94-L100)
- [\_\_getitem\_\_( ): return image, masks, tissue_type(as unknown), image_name](https://github.com/junlinguo/CellViT-Kidney/blob/main/cell_segmentation/datasets/pannuke_like_instance.py#L111).
- "single dummy tissue": Adrenal_gland. Just a placeholder and it does not affect the training objectives
- [loading instance mask](https://github.com/junlinguo/CellViT-Kidney/blob/main/cell_segmentation/datasets/pannuke_like_instance.py#L227-L245)
- [masks include: instance_map, nuclei_type_map (set to be the same as nuclei_binary map), nuclei_binary_map, hv_map](https://github.com/junlinguo/CellViT-Kidney/blob/main/cell_segmentation/datasets/pannuke_like_instance.py#L168)


### Customize 'base_ml/base_trainer.py'


### CellViT arch 

`/CellViT-kidney/models/segmentation/cell_segmentation/cellvit.py`


