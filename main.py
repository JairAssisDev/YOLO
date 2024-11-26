from ultralytics import YOLO

model = YOLO("yolo11n-cls.pt")

dataset = r"/home/jair/Documentos/YOLO/dataset"

model.train(data=dataset, epochs=200)