FROM nginx:1.28.0-alpine-slim
RUN addgroup -g 1001 nginxgroup && \
    adduser -D -G nginxgroup -u 1001 nginxuser && \
    mkdir -p /var/www/html && \
    chown -R nginxuser:nginxgroup /var/www/html /var/cache/nginx /var/log/nginx
WORKDIR /var/www/html
USER nginxuser
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]