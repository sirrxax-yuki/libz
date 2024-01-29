FROM python:3.11-slim-bullseye

# setup tzdata
ENV TZ Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime

# install required packages
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# install poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH "$PATH:/root/.local/bin"
RUN poetry config virtualenvs.create false

# backend
WORKDIR /backend
COPY pyproject.toml poetry.lock ./
RUN poetry install
