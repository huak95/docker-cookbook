FROM ultralytics/yolov5:v7.0-arm64

WORKDIR /usr/src/app
COPY yolo_test_image.jpg /usr/src/app/

CMD ['python3','segment/predict.py', \
     '--weights', 'yolov5s-seg.pt', \
     '--source', 'yolo_test_image.jpg', \
     '--exist-ok']

COPY 