<div align="center">
<h1>One Size Doesn't Fit All: Divide-and-Conquer Detector<br>for UAV Images</h1>
</div>

## Contents
- [Introduction](#introduction)
- [Install](#install)
- [Data Prepare](#data-prepare)
- [Train](#train)
- [Test](#test)

## Introduction

This is an official implementation of DICDet: **One Size Doesn't Fit All: Divide-and-Conquer Detector for UAV Images** by Pytorch.

### DICDet Performance on VisDrone2019-DET

| <span style="font-weight:normal;">Model</span> | <span style="font-weight:normal;">$\text{mAP}^{val}_{50}$<br>(%)</span> | <span style="font-weight:normal;">$\text{mAP}^{val}_{50:95}$<br>(%)</span> | <span style="font-weight:normal;">$\text{mAP}^{test}_{50}$<br>(%)</span> | <span style="font-weight:normal;">$\text{mAP}^{test}_{50:95}$<br>(%)</span> | <span style="font-weight:normal;">Params<br>(M)</span> | <span style="font-weight:normal;">FLOPs<br>(G)</span> | <span style="font-weight:normal;">Latency<br>(ms)</span> |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| DICDet-N | 36.6 | 21.7 | 29.6 | 17.0 | 1.5 | 6.8 | 3.7 |
| DICDet-S | 42.7 | 25.8 | 35.0 | 20.4 | 5.3 | 22.7 | 4.7 |
| DICDet-M | 46.2 | 28.4 | 37.7 | 22.2 | 16.4 | 71.7 | 6.4 |
| DICDet-L | 47.5 | 29.4 | 38.5 | 22.8 | 28.9 | 126.2 | 8.4 |
| DICDet-X | 49.1 | 30.8 | 40.3 | 24.1 | 37.3 | 166.3 | 10.9 |

## Install

Recommended Environment
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

### Download Dataset

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

1. Modify the dataset config to point to your data following the steps in **Data Prepare** part.

2. Set the model config and dataset config in `train.py`:

```python
model = YOLO("DICDet-S.yaml")  # choose from DICDet-N / S / M / L / X
model.train(data='ultralytics/cfg/datasets/VisDrone2019-DET.yaml', ...)
```

3. Run the script:

```python
python train.py
```

## Test

1. Modify the dataset config to point to your data following the steps in **Data Prepare** part.
2. Set the model weight and dataset config in `test.py`:

```python
model = YOLO("...best.pt")
model.val(data='ultralytics/cfg/datasets/VisDrone2019-DET.yaml', ...)
```

3. Run the script:

```python
python test.py
```
