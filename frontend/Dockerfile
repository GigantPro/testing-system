FROM node:19.6.0-alpine3.17 as build-deps

ENV NODE_ENV production
WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install --production

COPY ./ ./

RUN yarn build


FROM nginx:1.21.0-alpine as production
ENV NODE_ENV production

COPY --from=build-deps /app/build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]