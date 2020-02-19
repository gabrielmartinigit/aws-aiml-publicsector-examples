# Amazon Rekognition

O Amazon Rekognition facilita a adição de análises de imagem e vídeo aos seus aplicativos usando a tecnologia comprovada e altamente escalável de aprendizagem profunda, que não requer conhecimentos de machine learning para usar. Com o Amazon Rekognition, você pode identificar objetos, pessoas, texto, cenas e atividades em imagens e vídeos, além de detectar qualquer conteúdo inapropriado. O Amazon Rekognition também fornece recursos de análise facial e pesquisa facial altamente precisos que você pode usar para detectar, analisar e comparar rostos para uma ampla variedade de casos de uso de verificação de usuários, contagem de pessoas e segurança pública.

</br>
<p align="center"><img src="../../images/Rekognition.png" height="250" weight="250"/></p>
</br>

## Como executar

Iremos utilizar nesse laboratório a linguagem Python. Você pode instalar Python localmente, mas caso não queira, podemos subir um ambiente de desenvolvimento na AWS. Para isso, siga os procedimentos abaixo:

_Nota: Testar na região us-east-1 (N.Virginia)_

### Executando o CloudFormation para criar um notebook

1. [Clique aqui](cf-templates/../../../cf-templates/notebook.yml?Raw=true) para fazer o download do template que você usará para implantar a infraestrutura básica deste workshop.
2. Faça logon no [AWS Console](https://console.aws.amazon.com/console/home). Verifique se você está na região correta designada para este workshop.
3. Navegue para o console do CloudFormation: [https://console.aws.amazon.com/cloudformation/home](https://console.aws.amazon.com/cloudformation/home)
4. Lá, escolha **Create Stack**.
5. Na "Etapa 1 - Specify template", escolha **Upload a template file**.
6. Escolha o arquivo de modelo que você baixou na Etapa 1. Clique em **Next**.
7. Na "Etapa 2", digite o nome da pilha: **aiml-workshop**. Clique em **Next**.
8. No "Passo 3": basta clicar no botão **Next**.
9. Na "Etapa 4": ative a caixa de seleção **I acknowledge that AWS CloudFormation might create IAM resources.** e clique no botão **Create Stack**.

Aguarde até que todos os recursos sejam criados.

### Clonando o repositório

Após finalizar a criação do notebook, podemos ir para [https://console.aws.amazon.com/sagemaker/home?region=us-east-1#/notebook-instances](https://console.aws.amazon.com/sagemaker/home?region=us-east-1#/notebook-instances)

Ao abrir o notebook, iremos clonar esse repositório:

- Click em **New** e crie um novo terminal
- Execute os comandos abaixo:
  ```
  cd SageMaker
  git clone https://github.com/gabrielmartinigit/aws-aiml-publicsector-examples.git
  ```
- Feche o terminal

## Utilizando as APIs

O Rekognition entrega diferentes APIs que podemos utilizar. Essas são:

- Object and scene detection
- Image moderation
- Facial analysis
- Celebrity recognition
- Face comparison
- Text in image
- Video analysis

Para testar algumas dessas APIs iremos abrir o notebook **rekognition.ipynb** (estamos utilizando um notebook apenas para faciliar a demonstração. As APIs podem ser acessadas via qualquer script, o notebook não é um requisito.)

_Nota: Para executar as células do notebook basta clicar em **Run**. Após isso, aguarde a célula terminar o processamento até que \* vire um número._

## Utilizando Custom Labels

Com o Amazon Rekognition Custom Labels, você pode identificar os objetos e as cenas nas imagens que são específicos às necessidades dos seus negócios. Por exemplo, você pode criar um modelo para classificar peças específicas da máquina em sua linha de montagem ou detectar plantas não saudáveis. O Amazon Rekognition Custom Labels cuida do trabalho pesado do desenvolvimento de modelos para você, portanto, não é necessária experiência em machine learning. Você só precisa fornecer imagens de objetos ou cenas que deseja identificar e o serviço lida com o restante.

1. Importar dataset
2. Testar Bounding Box
3. Iniciar Treinamento
4. Start do modelo
5. Teste de inferência
6. Parar o modelo

## Referências

- Rekognition: https://aws.amazon.com/pt/rekognition/
- Boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- Custom Labels: https://aws.amazon.com/blogs/machine-learning/announcing-amazon-rekognition-custom-labels/

## License Summary

This sample code is made available under the MIT-0 license. See the LICENSE file.
