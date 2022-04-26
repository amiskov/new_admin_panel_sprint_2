FROM nginx:1.21-alpine

# Required for hiding Nginx version from headers
RUN apk update && apk add nginx-mod-http-headers-more

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx
COPY movies.conf /etc/nginx/conf.d
