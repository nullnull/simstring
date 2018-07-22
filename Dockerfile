FROM yamitzky/miniconda-neologd

WORKDIR /app

# to install mecab-python3
RUN apt-get update -qq && apt-get install -y build-essential

COPY env.yml /app
RUN conda env create --file /app/env.yml
RUN echo 'source activate simstring' > ~/.bashrc
