FROM ubuntu:16.04

LABEL maintainer="martinig"

# Defining some variables used at build time to install Python3
ARG PYTHON=python3
ARG PYTHON_PIP=python3-pip
ARG PIP=pip3
ARG PYTHON_VERSION=3.6.6

# Install some handful libraries like curl, wget, git, build-essential, zlib
RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    wget \
    git \
    libopencv-dev \
    openssh-client \
    openssh-server \
    vim \
    wget \
    python \
    nginx \
    zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Installing Python3
RUN wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz && \
    tar -xvf Python-$PYTHON_VERSION.tgz && cd Python-$PYTHON_VERSION && \
    ./configure && make && make install && \
    apt-get update && apt-get install -y --no-install-recommends libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev && \
    make && make install && rm -rf ../Python-$PYTHON_VERSION* && \
    ln -s /usr/local/bin/pip3 /usr/bin/pip

# Upgrading pip and creating symbolic link for python3
RUN ${PIP} --no-cache-dir install --upgrade pip
RUN ln -s $(which ${PYTHON}) /usr/local/bin/python

# Installing numpy, pandas, scikit-learn, scipy
RUN ${PIP} install --no-cache --upgrade \
    numpy==1.14.5 \
    pandas==0.24.1 \
    scikit-learn==0.20.3 \
    requests==2.21.0 \
    scipy==1.2.1

# Setting some environment variables.
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONUNBUFFERED=TRUE
ENV LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/local/lib"
ENV PYTHONIOENCODING=UTF-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY dummy_algorithm /opt/program
WORKDIR /opt/program