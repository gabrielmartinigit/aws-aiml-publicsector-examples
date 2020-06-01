# Start FROM Nvidia PyTorch image
FROM ubuntu:16.04

LABEL maintainer="martinig"


RUN apt-get -y update && apt-get install -y --no-install-recommends \
    wget \
    make \
    python \
    git \
    ca-certificates && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && \
    pip install numpy==1.16.2 scipy==1.2.1 scikit-learn==0.20.2 pandas flask gevent gunicorn && \
    ( \
    cd /usr/local/lib/python2.7/dist-packages/scipy/.libs \
    rm * \
    ln ../../numpy/.libs/* . \
    ) && rm -rf /root/.cache

# Install Darknet
COPY yolo_algorithm /opt/program
RUN cd /opt/program
RUN git clone https://github.com/AlexeyAB/darknet.git
RUN cd darknet
RUN make
RUN wget https://pjreddie.com/media/files/darknet53.conv.74

# Setting some environment variables.
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
WORKDIR /opt/program