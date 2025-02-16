#!/bin/bash

# Stop process by error
set -e

PROJECT_NAME="llm"

# when no arguments exists, use environment variable
IMAGE_UNAME="${1:-$USER}"
IMAGE_UID="${2:-$UID}"

IMAGE_TAG=${IMAGE_UNAME}_${PROJECT_NAME}

# output IMAGE_NAME and ...
echo IMAGE_UNAME=$IMAGE_UNAME IMAGE_UID=$IMAGE_UID
echo "Building image $IMAGE_TAG..."

# command to build Doceker image
docker build \
    -f docker/dockerfile \
    -t $IMAGE_TAG \
    --build-arg UNAME=$IMAGE_UNAME \
    --build-arg UID=$IMAGE_UID \
    .

echo "Image $IMAGE_TAG has been built successfully."