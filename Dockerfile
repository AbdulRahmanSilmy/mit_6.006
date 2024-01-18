FROM jupyter/base-notebook

WORKDIR /home/jovyan/work

USER root

RUN apt-get update && \
    echo 'yes' | apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID



