FROM nginx:latest

COPY Public	/var/www/html
COPY ./nginx.conf /etc/nginx/nginx.conf

WORKDIR /app

CMD ["nginx", "-g", "daemon off;"]
