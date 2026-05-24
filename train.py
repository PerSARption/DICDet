from ultralytics import YOLO

# Load a model
model = YOLO("DICDet-S.yaml")
model.train(data='ultralytics/cfg/datasets/VisDrone2019-DET.yaml', imgsz=640, epochs=500, batch=16, device=0, name='train')

# model.info()