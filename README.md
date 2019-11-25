# AWS SageMaker Public Sector Examples
Alguns exemplos de notebooks relacionados ao setor público.

_Pré requisitos:_
* Aumentar soft limit para instâncias de computação acelerada (https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
* Possuir IAM Role com acesso aos recursos:
    * Rekognition
    * Comprehend
    * Textract
    * SageMaker
    * S3
    * ECR

_Nota: Testado na região us-east-1 (N.Virginia)_


## Criando instância notebook no SageMaker
1. Crie um novo notebook em https://console.aws.amazon.com/sagemaker/
2. Em **instance_type** selecione o tamanho de máquina (Neste exemplo, iremos utilizar a instância c5.xlarge - você pode visualizar as especificações aqui https://aws.amazon.com/ec2/instance-types/)
3. Em **IAM Role**, selecione a Role já criada (AmazonSageMaker...)
4. Por fim, selecione **Create**

## Excutando os notebooks
1. Ao abrir o notebook, iremos clonar esse repositório:
    * Click em **New** e crie um novo terminal
    * Execute os comandos abaixo:    
        ```
            cd SageMaker
            git clone https://github.com/gabrielmartinigit/aws-sagemaker-publicsector-examples.git
        ```
    * Feche o terminal
2. Entre na pasta **aws-sagemaker-publicsector-example/notebooks**
3. Iremos abrir o primeiro notebook como exemplo, click no notebook chamado **ai-services-examples**
4. Escolha o kernel como **conda_python3**
5. Leia cada célula e execute para ver o resultado

## Limpando o ambiente
1. Termine o notebook
2. Termine os endpoints de inferência
3. Exclua os buckets criados
4. Exclua a role criada

## Referências
* https://github.com/awslabs/amazon-sagemaker-examples
* https://github.com/awslabs/amazon-sagemaker-mlops-workshop
* https://aws.amazon.com/blogs/machine-learning/deploy-trained-keras-or-tensorflow-models-using-amazon-sagemaker/
* https://course.fast.ai/start_sagemaker.html
* https://aws.amazon.com/blogs/machine-learning/building-training-and-deploying-fastai-models-with-amazon-sagemaker/

## License summary
This sample code is made available under the MIT-0 license. See the LICENSE file.
