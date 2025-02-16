#!/bin/bash

# Git Bash用

set -e

PROJECT_NAME="llm"
SN=${SN:-1}

IMAGE_UNAME="${1:-$USER}"
IMAGE_TAG=${IMAGE_UNAME}
CONTAINER_NAME=${IMAGE_UNAME}_${PROJECT_NAME}

# インタラクティブモード
# -it \
# バックグラウンド実行
# --detach \
# コンテナにすべてのGPU利用可能
# --gpus all \
# コンテナ終了時に自動で再起動
# --restart=always \
# 共有メモリサイズ
# --shm-size=8gb \
# コンテナ内でホストのデータにアクセス可
# --mount type=bind,source="/mnt/data${SN}",target="/home/${IMAGE_UNAME}/data" \
# Dockerボリュームをマウント（ファイル共有）
# --mount source=nfs-volume,target="/mnt/nfs" \
# Dockerボリュームをマウント（共有領域）
# --mount source=slum-volume,target="/mnt/slum" \   #修正必要
# コンテナ起動時の作業ディレクトリ
# --workdir "/home/${IMAGE_UNAME}" \
# 起動するコンテナのベースとなるDockerイメージの指定
# --name=$CONTAINER_NAME \

docker run \
    -it \
    --detach \
    --gpus all \
    --restart=always \
    --shm-size=64gb \
    --mount type=bind,source="//c/mnt/data${SN}",target="//c/mnt/ai_dev/${IMAGE_UNAME}/data" \
    --mount source=slum-volume,target="//mnt/slum" \
    --workdir "//c/mnt/ai_dev/${IMAGE_UNAME}" \
    --name=$CONTAINER_NAME \
    $IMAGE_TAG

echo "Container $CONTAINER_NAME has been started successfully."

# echo IP Address: $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_NAME)
