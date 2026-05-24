from ultralytics import YOLO

# Load a model
model = YOLO("runs/detect/train/weights/best.pt")
model.val(data='ultralytics/cfg/datasets/VisDrone2019-DET.yaml', imgsz=640, batch=16, device=0, split='test', name='test')

# model.info()