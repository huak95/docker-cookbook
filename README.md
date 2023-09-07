# docker-cookbook
learn docker

## ubuntu-hello
learn how to build simple docker
```bash
# build docker
cd ubuntu-hello
docker build . -t "ubuntu-hello"

# run docker
docker run -it --rm ubuntu-hello /bin/bash
docker run -it --rm ubuntu-hello
```

## python-fastapi
learn how to maintain docker with python env
```bash
cd python-fastapi
docker build . -t "python-fastapi"

docker run -it -p 8000:8000 --rm  python-fastapi 
```

## yolov5-yooo
learn how to use big docker images
```bash
cd yolov5-yooo
docker build . -t "yolov5-yooo"
docker run -it --rm yolov5-yooo /bin/bash

python3 segment/predict.py \
    --weights yolov5s-seg.pt --source 'yolo_test_image.jpg' --exist-ok

docker cp yolov5-yooo:runs/predict-seg/exp /runs # Can't copy results
```

## push docker container to AWS ECR

```bash 
# login to AWS ECR
aws ecr get-login-password --region ap-southeast-1 --profile bedrock_nonprod | docker login --username AWS --password-stdin 654934115675.dkr.ecr.ap-southeast-1.amazonaws.com

# build docker
docker buildx build --platform linux/amd64 . -t \
    654934115675.dkr.ecr.ap-southeast-1.amazonaws.com/python-fastapi

# push docker
docker push 654934115675.dkr.ecr.ap-southeast-1.amazonaws.com/python-fastapi

# run docker
docker run -it -p 8000:8000 --rm 654934115675.dkr.ecr.ap-southeast-1.amazonaws.com/python-fastapi
```

## BUILD X 
for building multiple platform in the sametime
