#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Step 1:
# Create dockerpath
# dockerpath=<your docker ID/path>
export DOCKER_ID_USER="gwtm11"
export DOCKER_CONTAINER_NAME="user_container"
dockerpath = gwtm11/$DOCKER_CONTAINER_NAME

# Step 2:  
# Authenticate & tag


#docker Login
docker login

# Step 3: 
#docker build
docker build --tag=$DOCKER_ID_USER/$DOCKER_CONTAINER_NAME:latest .


# docker tag frontend_container $DOCKER_ID_USER/frontend

#docker push
docker push $DOCKER_ID_USER/$DOCKER_CONTAINER_NAME:latest
# echo "Docker ID and Image: $dockerpath"

# Step 3:
# Push image to a docker repository
# docker push gwtm11/frontend_container
