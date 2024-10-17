from ultralytics import YOLO
import cv2

model = YOLO('yolo/yolov8l.pt')
results = model('images/zidane.jpg',show=True)

cv2.waitKey(0)

