# Constuindo seu próprio container para o Amazon SageMaker

Com o Amazon SageMaker, você pode empacotar seus próprios algoritmos que podem ser treinados e implantados no ambiente SageMaker.

Ao empacotar um algoritmo em um container, você pode trazer praticamente qualquer código para o ambiente Amazon SageMaker, independentemente da linguagem de programação, ambiente, estrutura ou dependência.

## Quando eu devo construir meu próprio container?

Pode não ser necessário criar um container para levar seu próprio código ao Amazon SageMaker. Ao usar um framework (como Apache MXNet ou TensorFlow) com suporte direto no SageMaker, você pode simplesmente fornecer o código Python que implementa seu algoritmo usando os pontos de entrada do SDK para esse framework. Esse conjunto de frameworks suportados está em constante expansão, portanto, recomendamos que você verifique a lista atual.

Se não houver suporte direto ao SDK para o seu ambiente, não se preocupe. É possível customizar a solução e neste neste repositório você pode encontrar como e alguns exemplos.

## Empacotando seu algoritmo

_Pré-requisitos:_

- Conhecimento básico de Docker;
- Conta da AWS com permissão ao Amazon ECR, Amazon S3 e Amazon SageMaker;
- AWS CLI V2 instalado e configurado em sua máquina;

### Como o Amazon SageMaker executa o container Docker

### O que você pode encontrar nesse repositório

## Referências

- https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/custom-training-containers
- https://github.com/aws/sagemaker-training-toolkit
- https://github.com/aws/sagemaker-inference-toolkit
- https://github.com/awslabs/amazon-sagemaker-examples/blob/master/advanced_functionality/tensorflow_bring_your_own/tensorflow_bring_your_own.ipynb
- https://github.com/awslabs/amazon-sagemaker-examples/blob/master/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.ipynb
- https://stackoverflow.com/questions/25185405/using-gpu-from-a-docker-container
- https://github.com/NVIDIA/nvidia-docker
- https://pjreddie.com/darknet/train-cifar/
- https://pypi.org/project/darknetpy/
- https://github.com/madhawav/YOLO3-4-Py
- https://github.com/ultralytics/yolov3
- https://github.com/ufoym/deepo
- https://ngc.nvidia.com/catalog/containers/?orderBy=modifiedDESC&pageNumber=5&query=&quickFilter=&filters=
