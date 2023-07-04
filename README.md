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