<div align="center">
<h1>One Size Doesn't Fit All: Divide-and-Conquer Detector<br>for UAV Images</h1>
</div>

## Content
- [Introduction](#introduction)
- [Install](#install)
- [Dataset](#dataset)
- [Train](#train)
- [Test](#test)

## Introduction

### Contributions
We propose a divide-and-conquer detector (DICDet) for UAV images that reasonably allocates computational resources. Firstly, a novel MRHNet as the backbone integrated with MRH module is proposed, which consists of multi-gradient flow, receptive field expansion, along with high-dimensional feature preservation. Secondly, a divide-and-conquer strategy guides the design of both the neck and head networks: a scale-specific neck network employs structures of different computation to process features of multi-size targets, and an asymmetric task-specific decoupled head is constructed to meet the feature requirements for localization and classification tasks respectively. Finally, we develop a new family of detectors with 5 model scales for UAV images: DICDet-N, S, M, L, and X.

### DICDet Performance on VisDrone2019-DET

| $\text{Model}$ | $\text{mAP}^{\text{val}}_{50}$(%) | $\text{mAP}^{\text{val}}_{50:95}$(%) | $\text{mAP}^{\text{test}}_{50}$(%) | $\text{mAP}^{\text{test}}_{50:95}$(%) | $\text{Params(M)}$ | $\text{FLOPs(G)}$ | $\text{Latency(ms)}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| DICDet-N | 36.6 | 21.7 | 29.6 | 17.0 | 1.5 | 6.8 | 3.7 |
| DICDet-S | 42.7 | 25.8 | 35.0 | 20.4 | 5.3 | 22.7 | 4.7 |
| DICDet-M | 46.2 | 28.4 | 37.7 | 22.2 | 16.4 | 71.7 | 6.4 |
| DICDet-L | 47.5 | 29.4 | 38.5 | 22.8 | 28.9 | 126.2 | 8.4 |
| DICDet-X | 49.1 | 30.8 | 40.3 | 24.1 | 37.3 | 166.3 | 10.9 |

## Install

**Recommended Environment**
- Python 3.8
- CUDA 11.7
- PyTorch 1.13.0

```shell
# Create a new conda environment
conda create -n dicdet python=3.8
conda activate dicdet

# Install PyTorch
pip install torch==1.13.0+cu117 torchvision==0.14.0+cu117 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cu117

# Clone the repository and install dependencies
git clone https://github.com/PerSARption/DICDet.git
cd DICDet
pip install -r requirements.txt
```

## Data Prepare

### Dataset
- [VisDrone2019-DET](https://github.com/VisDrone/VisDrone-Dataset)
- [AI-TOD-v2](https://chasel-tsui.github.io/AI-TOD-v2/)
- [DOTA-v1.0](https://captain-whu.github.io/DOTA/index.html)

### Directory Structure of the Dataset

DICDet follows the **YOLO format** for dataset annotations.

```
└── VisDrone
    ├── VisDrone2019-DET-train
    │   ├── images
    │   └── labels
    ├── VisDrone2019-DET-val
    │   ├── images
    │   └── labels
    └── VisDrone2019-DET-test-dev
        ├── images
        └── labels
```

### Config file selection

For VisDrone2019-DET dataset, please select the config file `ultralytics/cfg/datasets/VisDrone2019-DET.yaml`

For AI-TOD-v2 dataset, please select the config file `ultralytics/cfg/datasets/AI-TOD.yaml`

For DOTA-v1.0 dataset, please select the config file `ultralytics/cfg/datasets/DOTAv1.yaml`

## Train

### Training

1. Modify the dataset config to point to your data following the steps in **Data Prepare** part

2. Set the model config and dataset config in `train.py`:

```python
model = YOLO("DICDet-S.yaml")  # choose from DICDet-N / S / M / L / X
model.train(data='ultralytics/cfg/datasets/VisDrone2019-DET.yaml', ...)
```

3. Run the script:

```python
python train.py
```

### Test

1. Modify the dataset config to point to your data following the steps in **Data Prepare** part.
2. Set the model weight and dataset config in `test.py`:

```python
model = YOLO("...best.pt")  
model.test(data='ultralytics/cfg/datasets/VisDrone2019-DET.yaml', ...)
```

3. Run the script:

```python
python test.py
```
