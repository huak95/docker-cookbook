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