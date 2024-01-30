#!/bin/sh

AWS_REGISTRY=$(aws ssm get-parameter --query "Parameter.Value" --output text --name /libz/ecr/endpoint)
IMAGE_TAG=$(cat /app/artifacts.json | jq -r '.imageTag')

aws ecr get-login-password | docker login --username AWS --password-stdin ${AWS_REGISTRY}
docker pull ${IMAGE_TAG}
