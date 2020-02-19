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
PROJECT = "arn:aws:rekognition:us-east-1:709545988742:project/ppe-detection/1580784227457"
PROJECT_VERSION = "arn:aws:rekognition:us-east-1:709545988742:project/ppe-detection/version/ppe-detection.2020-02-03T23.52.27/1580784754596"
# PROJECT_VERSION = "REKOGNITION ARN"
IMAGE_TEST = {
    # 'Bytes': b'bytes', -> you can also use image base64
    'S3Object': {
        'Bucket': 'martinig-dataset',
        'Name': 'yellow/10_yellow.jpg'
    }
}


def verify_rekognition_custom():
    response = REKOGNITION_CLIENT.describe_project_versions(
        ProjectArn='arn:aws:rekognition:us-east-1:709545988742:project/ppe-detection/1580784227457',
        VersionNames=['ppe-detection.2020-02-03T23.52.27']
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
        start_rekognition_custom()

    # stop model
    # status = stop_rekognition_custom()
    # print(status)
    # print('Stopping')


if __name__ == "__main__":
    app()
