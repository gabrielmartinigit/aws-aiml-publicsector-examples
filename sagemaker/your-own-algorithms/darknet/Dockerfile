# Start FROM Nvidia PyTorch image
FROM nvcr.io/nvidia/pytorch:20.03-py3

LABEL maintainer="martinig"

# Install dependencies
RUN apt-get update
COPY ./requirements.txt /opt/program/requirements.txt
WORKDIR /opt/program
RUN pip install -r requirements.txt

# Setting some environment variables.
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY yolo_algorithm /opt/program