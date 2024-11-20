# Используем официальный образ Nginx на базе Alpine Linux для легковесности
FROM nginx:stable-alpine

# Удаляем стандартный сайт Nginx
RUN rm -rf /usr/share/nginx/html/*

# Копируем ваши статические файлы в директорию, обслуживаемую Nginx
COPY . /usr/share/nginx/html

# Открываем порт 80 для доступа к приложению
EXPOSE 80

# Запускаем Nginx в форграунд режиме
CMD ["nginx", "-g", "daemon off;"]