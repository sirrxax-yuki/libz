FROM ubuntu:24.04

ARG RSI_CLIENT_ID=xxxxxxxx
ARG RSI_AUTH_REDIRECT_URL=https://www.example.com/login/redirect

# setup tzdata
ENV TZ Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime

# preinstall nodejs
RUN apt-get update -y && apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_21.x | bash -

# install required packages
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y \
    nodejs \
    python3 \
    pip \
    nginx \
    nginx-extras \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3 /usr/bin/python

# install poetry for backend
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH "$PATH:/root/.local/bin"
RUN poetry config virtualenvs.create false

# backend
WORKDIR /backend
COPY backend/pyproject.toml backend/poetry.lock ./
RUN poetry install
COPY backend .

# frontend
WORKDIR /frontend
ENV VITE_RSI_CLIENT_ID ${RSI_CLIENT_ID}
ENV VITE_RSI_AUTH_REDIRECT_URL ${RSI_AUTH_REDIRECT_URL}
COPY frontend/package*.json ./
RUN npm install
COPY frontend .
RUN npm run build

# tools
WORKDIR /tools
COPY tools .

# deployment server
WORKDIR /
COPY server/nginx.conf /etc/nginx/nginx.conf
COPY server/production.d /etc/nginx/conf.d

CMD /bin/bash -c "nginx -g 'daemon off;' & uvicorn backend.src.main:app --host 0.0.0.0 --port 3304 --reload"
