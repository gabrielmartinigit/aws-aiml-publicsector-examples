# Constuindo seu próprio container para o Amazon SageMaker

Com o Amazon SageMaker, você pode empacotar seus próprios algoritmos que podem ser treinados e implantados no ambiente SageMaker. Este README o guiará através de um exemplo que mostra como construir um container Docker para SageMaker e utilizar os algoritmos das redes neurais Darknet para treinamento e inferência.

Ao empacotar um algoritmo em um container, você pode trazer praticamente qualquer código para o ambiente Amazon SageMaker, independentemente da linguagem de programação, ambiente, estrutura ou dependência.

##

## References

- https://github.com/awslabs/amazon-sagemaker-examples/tree/master/advanced_functionality/custom-training-containers
- https://github.com/aws/sagemaker-training-toolkit
- https://github.com/aws/sagemaker-inference-toolkit
- https://github.com/awslabs/amazon-sagemaker-examples/blob/master/advanced_functionality/tensorflow_bring_your_own/tensorflow_bring_your_own.ipynb
- https://github.com/awslabs/amazon-sagemaker-examples/blob/master/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.ipynb
- https://stackoverflow.com/questions/25185405/using-gpu-from-a-docker-container
- https://github.com/NVIDIA/nvidia-docker
- https://pjreddie.com/darknet/train-cifar/
- https://pypi.org/project/darknetpy/
