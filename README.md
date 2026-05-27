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

<table style="width:100%; text-align:center; border-collapse:collapse;">
  <thead>
    <tr>
      <th style="padding:8px; border:1px solid #ddd; font-weight:normal; white-space:nowrap;">Model</th>
      <th style="padding:8px; border:1px solid #ddd; font-weight:normal; white-space:nowrap;">mAP<sup>val</sup><sub>50</sub>(%)</th>
      <th style="padding:8px; border:1px solid #ddd; font-weight:normal; white-space:nowrap;">mAP<sup>val</sup><sub>50:95</sub>(%)</th>
      <th style="padding:8px; border:1px solid #ddd; font-weight:normal; white-space:nowrap;">mAP<sup>test</sup><sub>50</sub>(%)</th>
      <th style="padding:8px; border:1px solid #ddd; font-weight:normal; white-space:nowrap;">mAP<sup>test</sup><sub>50:95</sub>(%)</th>
      <th style="padding:8px; border:1px solid #ddd; font-weight:normal; white-space:nowrap;">Params(M)</th>
      <th style="padding:8px; border:1px solid #ddd; font-weight:normal; white-space:nowrap;">FLOPs(G)</th>
      <th style="padding:8px; border:1px solid #ddd; font-weight:normal; white-space:nowrap;">Latency(ms)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; white-space:nowrap;">DICDet-N</td>
      <td style="padding:8px; border:1px solid #ddd;">36.6</td>
      <td style="padding:8px; border:1px solid #ddd;">21.7</td>
      <td style="padding:8px; border:1px solid #ddd;">29.6</td>
      <td style="padding:8px; border:1px solid #ddd;">17.0</td>
      <td style="padding:8px; border:1px solid #ddd;">1.5</td>
      <td style="padding:8px; border:1px solid #ddd;">6.8</td>
      <td style="padding:8px; border:1px solid #ddd;">3.7</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; white-space:nowrap;">DICDet-S</td>
      <td style="padding:8px; border:1px solid #ddd;">42.7</td>
      <td style="padding:8px; border:1px solid #ddd;">25.8</td>
      <td style="padding:8px; border:1px solid #ddd;">35.0</td>
      <td style="padding:8px; border:1px solid #ddd;">20.4</td>
      <td style="padding:8px; border:1px solid #ddd;">5.3</td>
      <td style="padding:8px; border:1px solid #ddd;">22.7</td>
      <td style="padding:8px; border:1px solid #ddd;">4.7</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; white-space:nowrap;">DICDet-M</td>
      <td style="padding:8px; border:1px solid #ddd;">46.2</td>
      <td style="padding:8px; border:1px solid #ddd;">28.4</td>
      <td style="padding:8px; border:1px solid #ddd;">37.7</td>
      <td style="padding:8px; border:1px solid #ddd;">22.2</td>
      <td style="padding:8px; border:1px solid #ddd;">16.4</td>
      <td style="padding:8px; border:1px solid #ddd;">71.7</td>
      <td style="padding:8px; border:1px solid #ddd;">6.4</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; white-space:nowrap;">DICDet-L</td>
      <td style="padding:8px; border:1px solid #ddd;">47.5</td>
      <td style="padding:8px; border:1px solid #ddd;">29.4</td>
      <td style="padding:8px; border:1px solid #ddd;">38.5</td>
      <td style="padding:8px; border:1px solid #ddd;">22.8</td>
      <td style="padding:8px; border:1px solid #ddd;">28.9</td>
      <td style="padding:8px; border:1px solid #ddd;">126.2</td>
      <td style="padding:8px; border:1px solid #ddd;">8.4</td>
    </tr>
    <tr>
      <td style="padding:8px; border:1px solid #ddd; white-space:nowrap;">DICDet-X</td>
      <td style="padding:8px; border:1px solid #ddd;">49.1</td>
      <td style="padding:8px; border:1px solid #ddd;">30.8</td>
      <td style="padding:8px; border:1px solid #ddd;">40.3</td>
      <td style="padding:8px; border:1px solid #ddd;">24.1</td>
      <td style="padding:8px; border:1px solid #ddd;">37.3</td>
      <td style="padding:8px; border:1px solid #ddd;">166.3</td>
      <td style="padding:8px; border:1px solid #ddd;">10.9</td>
    </tr>
  </tbody>
</table>

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
