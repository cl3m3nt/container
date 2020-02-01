# docker pre-req
docker --version

docker info

# https://docs.docker.com/docker-for-mac/
docker run hello-world

# list docker local images
docker images

# list locally running container
docker container ls -a
docker ps

# build an image based on Dockerfile
docker build -t flask-tutorial:latest .

# run flask container based on previous image
docker run -d -p 5000:5000 flask-tutorial

# deploy a container based on an nginx docker image
docker run --detach --publish=8081:80 --name=webserver1 nginx

# prune stopped containers
docker container prune

# docker container logs - to get container logs in case of error when run
docker container logs <container-id>

# docker new image and container full process
https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/#step-testing-nginx-and-phpfpm-in-the-container

# docker build an image
docker build -t nginx_image .

# docker run ubuntu 16.04 image with Nginx & PHP
docker run -d -v /webroot:/var/www/html -p 9081:80 --name nginx_php_1 nginx_php_image

# start a stopped container
docker container start <container-id>

# connect to a docker container: https://phase2.github.io/devtools/common-tasks/ssh-into-a-container/
docker exec -it <container-name> /bin/bash



############ docker images Dockerfile examples ############

# nginx-php app on Ubuntu 16.04 Docker Image
https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/

# flask app on Ubuntu 16.04 Docker Image
https://runnable.com/docker/python/dockerize-your-flask-application

# cuda 9.0 base
https://gitlab.com/nvidia/container-images/cuda/blob/master/dist/ubuntu16.04/9.0/base/Dockerfile


############ docker build Images & run Container ############

# docker pull a built image
docker pull tensorflow/tensorflow:1.12.3-py3

# docker build an image
docker build -t <image-name> .
docker build -t nginx_image . # nginx-php app container build
docker build -t flask-tutorial:latest . # flask app container build
docker build -t cuda9.0base:latest . # flask app container build

# docker run an image
docker run -d -v /webroot:/var/www/html -p 9081:80 --name nginx_php_1 nginx_php_image # run nginx-php app container
docker run -d -p 5000:5000 flask-tutorial # run flask app container
docker run -d cuda9.0base -p 6000:80
docker run -d tensorflow/tensorflow  

############ operation on container ############
# container status
docker ps
docker container ls -a

# connect to a docker container
docker exec -it <container-name> /bin/bash