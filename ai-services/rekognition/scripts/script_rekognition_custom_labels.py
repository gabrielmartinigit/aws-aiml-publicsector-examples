# -*- coding: utf-8 -*-
'''
Esse script demonstra como utilizar a API do Rekognition Custom Label em Python.
Após criar um modelo customizado, basta substituir o valor do PROJECT_VERSION.
Para testar é necessário dar o start no modelo (em torno de 5 minutos) e depois enviar uma imagem para detecção.
Essa imagem pode estar em um bucket S3 ou pode ser enviada em bytes.
Finalizando o seu teste, basta utilizar a função de stop do script.
'''

import boto3

REKOGNITION_CLIENT = boto3.client('rekognition')
PROJECT = "PROJECT_ARN"
PROJECT_VERSION = "PROJECT_VERSION_ARN"
VERSION_NAME = "VERSION_NAME"

IMAGE_TEST = {
    # 'Bytes': b'bytes', -> you can also use image base64
    'S3Object': {
        'Bucket': 'BUCKET CRIADO',
        'Name': 'yellow/10_yellow.jpg'
    }
}


def verify_rekognition_custom():
    response = REKOGNITION_CLIENT.describe_project_versions(
        ProjectArn=PROJECT,
        VersionNames=[VERSION_NAME]
    )
    return response['ProjectVersionDescriptions'][0]['Status']


def detect_rekognition_custom(image):
    response = REKOGNITION_CLIENT.detect_custom_labels(
        ProjectVersionArn=PROJECT_VERSION,
        Image=image,
        MaxResults=123,
        MinConfidence=80
    )
    return response['CustomLabels'][0]


def start_rekognition_custom():
    response = REKOGNITION_CLIENT.start_project_version(
        ProjectVersionArn=PROJECT_VERSION,
        MinInferenceUnits=5
    )
    return response


def stop_rekognition_custom():
    response = REKOGNITION_CLIENT.stop_project_version(
        ProjectVersionArn=PROJECT_VERSION
    )
    return response['Status']


def app():
    # verify if model is started
    status = verify_rekognition_custom()
    print(status)
    if status == 'RUNNING':
        # detect label
        label = detect_rekognition_custom(IMAGE_TEST)
        print(label)
    else:
        # start model
        print("Starting the model")
        start_rekognition_custom()

    # stop model
    # status = stop_rekognition_custom()
    # print(status)
    # print('Stopping')


if __name__ == "__main__":
    app()
