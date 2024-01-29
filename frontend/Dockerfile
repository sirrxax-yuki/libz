FROM node:21.6-bookworm-slim

ARG RSI_CLIENT_ID=xxxxxxxx
ARG RSI_AUTH_REDIRECT_URL=https://www.example.com/login/redirect

# setup tzdata
ENV TZ Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime

# frontend
WORKDIR /frontend
ENV VITE_RSI_CLIENT_ID ${RSI_CLIENT_ID}
ENV VITE_RSI_AUTH_REDIRECT_URL ${RSI_AUTH_REDIRECT_URL}
COPY ./package*.json ./
RUN npm install
COPY . .
RUN npm run build
