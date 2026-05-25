# One Size Doesn't Fit All: Divide-and-Conquer Detector for UAV Images

## Introduction

This is an official implementation of **One Size Doesn't Fit All: Divide-and-Conquer Detector for UAV Images** by **Pytorch**.

### Data Prepare

- [VisDrone2019-DET](https://github.com/VisDrone/VisDrone-Dataset)
- [DOTA-v1.0](https://captain-whu.github.io/DOTA/index.html)
- [AI-TOD-v2](https://chasel-tsui.github.io/AI-TOD-v2/)

```
For VisDrone2019-DET:
-datasets
--VisDrone2019-DET
----images (includes UAV images, .jpg)
----annotations (includes annotations, .txt)
```

### Config file selection

For VisDrone2019-DET dataset, please select the config file `ultralytics/cfg/datasets/VisDrone2019-DET.yaml`

For AI-TOD-v2 dataset, please select the config file `ultralytics/cfg/datasets/AI-TOD-v2.yaml`

For DOTA-v1.0 dataset, please select the config file `ultralytics/cfg/datasets/DOTA-v1.0.yaml`

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

4. Run the script:

```python
python test.py
```
