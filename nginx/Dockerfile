FROM nginx:1.23.3-alpine

RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/

EXPOSE 83

CMD ["nginx", "-g", "daemon off;"]
