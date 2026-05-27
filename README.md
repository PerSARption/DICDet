<div align="center">
<h1>DICDet: One Size Doesn't Fit All: Divide-and-Conquer Detector for UAV Images</h1>
</div>

## Contents
- [Introduction](#introduction)
- [Install](#install)
- [Dataset](#dataset)
- [Train](#train)
- [Model Config](#model-config)
- [Test](#test)

## Introduction

### Contributions
We propose a divide-and-conquer detector (DICDet) for UAV images that reasonably allocates computational resources. Firstly, a novel MRHNet as the backbone integrated with MRH module is proposed, which consists of multi-gradient flow, receptive field expansion, along with high-dimensional feature preservation. Secondly, a divide-and-conquer strategy guides the design of both the neck and head networks: a scale-specific neck network employs structures of different computation to process features of multi-size targets, and an asymmetric task-specific decoupled head is constructed to meet the feature requirements for localization and classification tasks respectively. Finally, we develop a new family of detectors with 5 model scales for UAV images: DICDet-N, S, M, L, and X.

### DICDet Performance on VisDrone2019-DET

<table style="text-align: center; caption-side: top; margin:auto; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="text-align:center; padding:8px; border:1px solid #ddd;">Model</th>
      <th style="text-align:center; padding:8px; border:1px solid #ddd;">$\text{mAP}^{\text{val}}_{50}$(%)</th>
      <th style="text-align:center; padding:8px; border:1px solid #ddd;">$\text{mAP}^{\text{val}}_{50:95}$(%)</th>
      <th style="text-align:center; padding:8px; border:1px solid #ddd;">$\text{mAP}^{\text{test}}_{50}$(%)</th>
      <th style="text-align:center; padding:8px; border:1px solid #ddd;">$\text{mAP}^{\text{test}}_{50:95}$(%)</th>
      <th style="text-align:center; padding:8px; border:1px solid #ddd;">Params(M)</th>
      <th style="text-align:center; padding:8px; border:1px solid #ddd;">FLOPs(G)</th>
      <th style="text-align:center; padding:8px; border:1px solid #ddd;">Latency(ms)</th>
    </tr>
  </thead>
  <tbody>
    <tr align="center">
      <td style="padding:8px; border:1px solid #ddd;"><b>DICDet-N</b></td>
      <td style="padding:8px; border:1px solid #ddd;">36.6</td>
      <td style="padding:8px; border:1px solid #ddd;">21.7</td>
      <td style="padding:8px; border:1px solid #ddd;">29.6</td>
      <td style="padding:8px; border:1px solid #ddd;">17.0</td>
      <td style="padding:8px; border:1px solid #ddd;">1.5</td>
      <td style="padding:8px; border:1px solid #ddd;">6.8</td>
      <td style="padding:8px; border:1px solid #ddd;">3.7</td>
    </tr>
    <tr align="center">
      <td style="padding:8px; border:1px solid #ddd;"><b>DICDet-S</b></td>
      <td style="padding:8px; border:1px solid #ddd;">42.7</td>
      <td style="padding:8px; border:1px solid #ddd;">25.8</td>
      <td style="padding:8px; border:1px solid #ddd;">35.0</td>
      <td style="padding:8px; border:1px solid #ddd;">20.4</td>
      <td style="padding:8px; border:1px solid #ddd;">5.3</td>
      <td style="padding:8px; border:1px solid #ddd;">22.7</td>
      <td style="padding:8px; border:1px solid #ddd;">4.7</td>
    </tr>
    <tr align="center">
      <td style="padding:8px; border:1px solid #ddd;"><b>DICDet-M</b></td>
      <td style="padding:8px; border:1px solid #ddd;">46.2</td>
      <td style="padding:8px; border:1px solid #ddd;">28.4</td>
      <td style="padding:8px; border:1px solid #ddd;">37.7</td>
      <td style="padding:8px; border:1px solid #ddd;">22.2</td>
      <td style="padding:8px; border:1px solid #ddd;">16.4</td>
      <td style="padding:8px; border:1px solid #ddd;">71.7</td>
      <td style="padding:8px; border:1px solid #ddd;">6.4</td>
    </tr>
    <tr align="center">
      <td style="padding:8px; border:1px solid #ddd;"><b>DICDet-L</b></td>
      <td style="padding:8px; border:1px solid #ddd;">47.5</td>
      <td style="padding:8px; border:1px solid #ddd;">29.4</td>
      <td style="padding:8px; border:1px solid #ddd;">38.5</td>
      <td style="padding:8px; border:1px solid #ddd;">22.8</td>
      <td style="padding:8px; border:1px solid #ddd;">28.9</td>
      <td style="padding:8px; border:1px solid #ddd;">126.2</td>
      <td style="padding:8px; border:1px solid #ddd;">8.4</td>
    </tr>
    <tr align="center">
      <td style="padding:8px; border:1px solid #ddd;"><b>DICDet-X</b></td>
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

```shell
git clone https://github.com/YOUYOUPark/DICDet.git
cd DICDet
pip install -e ".[dev]"
```

## Dataset

- [VisDrone2019-DET](https://github.com/VisDrone/VisDrone-Dataset)
- [AI-TOD-v2](https://chasel-tsui.github.io/AI-TOD-v2/)
- [DOTA-v1.0](https://captain-whu.github.io/DOTA/index.html)

```
For VisDrone2019-DET:
-datasets
--VisDrone2019-DET
----images (includes UAV images, .jpg)
----annotations (includes annotations, .txt)

For AI-TOD-v2:
-datasets
--AI-TOD-v2
----images (includes aerial images, .png)
----annotations (includes annotations, .txt)

For DOTA-v1.0:
-datasets
--DOTA-v1.0
----images (includes aerial images, .png)
----labelTxt (includes annotations, .txt)
```

### Config file selection

For VisDrone2019-DET dataset, please select the config file `ultralytics/cfg/datasets/VisDrone2019-DET.yaml`

For AI-TOD-v2 dataset, please select the config file `ultralytics/cfg/datasets/AI-TOD.yaml`

For DOTA-v1.0 dataset, please select the config file `ultralytics/cfg/datasets/DOTAv1.yaml`

## Train

1. Set the model config and dataset config in `train.py`:

```python
model = YOLO("DICDet-S.yaml")  # choose from DICDet-N / S / M / L / X
model.train(data='ultralytics/cfg/datasets/VisDrone2019-DET.yaml', ...)
```

2. Run the script:

```shell
python train.py
```

## Model Config

<table style="text-align:center; margin:auto; border-collapse: collapse;">
  <thead>
    <tr style="background-color: #f5f5f5;">
      <th style="padding: 8px; border: 1px solid #ddd;">Model</th>
      <th style="padding: 8px; border: 1px solid #ddd;">Config</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: left;">DICDet-N</td>
      <td style="padding: 8px; border: 1px solid #ddd;"><a href="./ultralytics/cfg/models/DICDet/DICDet-N.yaml">DICDet-N.yaml</a></td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: left;">DICDet-S</td>
      <td style="padding: 8px; border: 1px solid #ddd;"><a href="./ultralytics/cfg/models/DICDet/DICDet-S.yaml">DICDet-S.yaml</a></td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: left;">DICDet-M</td>
      <td style="padding: 8px; border: 1px solid #ddd;"><a href="./ultralytics/cfg/models/DICDet/DICDet-M.yaml">DICDet-M.yaml</a></td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: left;">DICDet-L</td>
      <td style="padding: 8px; border: 1px solid #ddd;"><a href="./ultralytics/cfg/models/DICDet/DICDet-L.yaml">DICDet-L.yaml</a></td>
    </tr>
    <tr>
      <td style="padding: 8px; border: 1px solid #ddd; text-align: left;">DICDet-X</td>
      <td style="padding: 8px; border: 1px solid #ddd;"><a href="./ultralytics/cfg/models/DICDet/DICDet-X.yaml">DICDet-X.yaml</a></td>
    </tr>
  </tbody>
</table>

## Test

1. Modify the dataset config to point to your data following the steps in **Dataset** part.
2. Set your model path following the steps in **Train** part.
3. Run the script:

```shell
python test.py
```
