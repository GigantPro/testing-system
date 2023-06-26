FROM node:19.6.0-alpine3.17 as build-deps

# ENV NODE_ENV production
WORKDIR /app

COPY ./package.json ./yarn.lock ./
RUN yarn install

COPY . .

RUN yarn build

EXPOSE 5002

CMD [ "node", ".output/server/index.mjs" ]