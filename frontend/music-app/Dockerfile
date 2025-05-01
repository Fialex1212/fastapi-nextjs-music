FROM node:20 AS builder

WORKDIR /app

COPY package.json yarn.lock ./

# Сначала установка зависимостей — без копирования src
RUN yarn install

# Потом копируем остальное
COPY . .

# Убедимся, что lightningcss работает
RUN yarn postinstall || true

RUN yarn build

CMD ["yarn", "start"]