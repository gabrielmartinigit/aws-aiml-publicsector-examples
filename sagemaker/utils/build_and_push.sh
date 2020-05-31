#!/usr/bin/env bash

# This script shows how to build the Docker image and push it to ECR to be ready for use
# by SageMaker.

# The argument to this script is the image name. This will be used as the image on the local
# machine and combined with the account and region to form the repository name for ECR.
image=$1
algorithm_folder=$2

if [ "$image" == "" ]; then
    echo "Usage: $0 <image-name> <algorithm_folder>"
    exit 1
fi

if [ "$algorithm_folder" == "" ]; then
    echo "Usage: $0 <image-name> <algorithm_folder>"
    exit 1
fi

echo "Iniciando o build da imagem Docker..."

cp ../../utils/server/* $algorithm_folder/
chmod +x $algorithm_folder/train
chmod +x $algorithm_folder/serve

# Get the account number associated with the current IAM credentials
account=$(aws sts get-caller-identity --query Account --output text)
echo "AWS ID: ${account}"

if [ $? -ne 0 ]; then
    exit 255
fi

# Get the region defined in the current configuration (default to us-east-1 if none defined)
region=$(aws configure get region)
region=${region:-us-east-1}
echo "Região: ${region}"

fullname="${account}.dkr.ecr.${region}.amazonaws.com/${image}:latest"

# If the repository doesn't exist in ECR, create it.

aws ecr describe-repositories --repository-names "${image}" >/dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Criando repositório ${image} no ECR"
    aws ecr create-repository --repository-name "${image}" >/dev/null
fi

# Get the login command from ECR and execute it directly
aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${account}.dkr.ecr.${region}.amazonaws.com

# Build the docker image locally with the image name and then push it to ECR
# with the full name.

docker build -t ${image} .
docker tag ${image} ${fullname}

echo "Iniciando o push para o repositório..."
docker push ${fullname}

echo "Push da imagem efetuado com sucesso!"
