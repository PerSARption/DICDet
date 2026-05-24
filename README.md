# DICDet: One Size Doesn't Fit All: Divide-and-Conquer Detector for UAV Images

[Paper]() |

## Introduce

This is an official implementation of **DICDet: One Size Doesn't Fit All: Divide-and-Conquer Detector for UAV Images** by **Pytorch**.

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

For DOTA-v1.0:
-datasets
--DOTA-v1.0
----images (includes aerial images, .png)
----labelTxt (includes annotations, .txt)

For AI-TOD-v2:
-datasets
--AI-TOD-v2
----images (includes aerial images, .png)
----annotations (includes annotations, .txt)
```

### Config file selection

For VisDrone2019-DET dataset, please select the config file `ultralytics/cfg/datasets/VisDrone2019-DET.yaml`

For DOTA-v1.0 dataset, please select the config file `ultralytics/cfg/datasets/DOTAv1.yaml`

For AI-TOD-v2 dataset, please select the config file `ultralytics/cfg/datasets/AI-TOD.yaml`

### Training/Resume Training

1. Set the model config and dataset config in `train.py`:

```python
model = YOLO("DICDet-S.yaml")  # choose from DICDet-N / S / M / L / X
model.train(data='ultralytics/cfg/datasets/VisDrone2019-DET.yaml', ...)
```

2. Run the script:

```python
python train.py
```

### Test

1. Modify the dataset config to point to your data following the steps in **Data Prepare** part.
2. Set your model path following the steps in **Training/Resume Training** part.
3. Run the script:

```python
python test.py
```
