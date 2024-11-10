from ultralytics import YOLO

model = YOLO("yolo11n-cls.pt")

dataset = r"C:\Users\jair\PycharmProjects\ouvido\dataset"

model.train(data=dataset, epochs=20)