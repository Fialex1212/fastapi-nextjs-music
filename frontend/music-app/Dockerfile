FROM node:23-slim AS builder

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

RUN yarn postinstall || true

RUN yarn build

CMD ["yarn", "start"]