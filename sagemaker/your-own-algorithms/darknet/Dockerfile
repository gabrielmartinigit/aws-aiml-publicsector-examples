# Start FROM Nvidia PyTorch image
FROM python:3.6-alpine

LABEL maintainer="martinig"

# Install dependencies
COPY ./requirements.txt /opt/program/requirements.txt
RUN pip install -r /opt/program/requirements.txt

# Setting some environment variables.
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY yolo_algorithm /opt/program
WORKDIR /opt/program