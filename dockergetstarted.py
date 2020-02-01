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

# nginx-php app on Ubuntu 16.04 Docker Image
https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/

# flask app on Ubuntu 16.04 Docker Image
https://runnable.com/docker/python/dockerize-your-flask-application