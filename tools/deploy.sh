#!/bin/sh

AWS_REGISTRY=$(aws ssm get-parameter --query "Parameter.Value" --output text --name /libz/ecr/endpoint)
AWS_DATABASE=$(aws ssm get-parameter --query "Parameter.Value" --output text --name /libz/db/endpoint)
AWS_DATABASE_USER=$(aws ssm get-parameter --query "Parameter.Value" --output text --name /libz/db/user)
AWS_DATABASE_PASSWORD=$(aws ssm get-parameter --query "Parameter.Value" --output text --name /libz/db/password --with-decryption)
IMAGE_TAG=$(cat artifacts.json | jq -r '.imageTag')

docker rm -f libz-app 2>/dev/null

aws ecr get-login-password | docker login --username AWS --password-stdin ${AWS_REGISTRY}

which jq
echo ${IMAGE_TAG}

docker pull ${IMAGE_TAG}

docker run \
    --name libz-app \
    -p 80:80 \
    -e DATABASE_HOST=${AWS_DATABASE} \
    -e DATABASE_PORT=3306 \
    -e DATABASE_USER=${AWS_DATABASE_USER} \
    -e DATABASE_PASSWORD=${AWS_DATABASE_PASSWORD} \
    -e DATABASE_NAME=libz \
    -d ${IMAGE_TAG}
