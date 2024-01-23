FROM jupyter/base-notebook

WORKDIR /home/jovyan/work

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

USER root

RUN apt-get update && \
    echo 'yes' | apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID



