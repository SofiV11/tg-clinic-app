FROM node:18

WORKDIR /home/node/app

COPY package*.json ./

RUN npm install

COPY . .


# Опционально: документирует, что приложение слушает на порту 3000
# EXPOSE 3000

