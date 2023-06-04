# Продуктовый помощник Foodgram - дипломный проект студента 49 когорты Яндекс.Практикум 2022-2023 гг. Трушечкина Р.Б.

![workflow bagde](https://github.com/Rostislaff/foodgram-project-react/actions/workflows/foodgram.yml/badge.svg)

## Описание проекта Foodgram
«Продуктовый помощник»: приложение, на котором пользователи публикуют рецепты кулинарных изделий, подписываться на публикации других авторов и добавлять рецепты в свое избранное.
Сервис «Список покупок» позволит пользователю создавать список продуктов, которые нужно купить для приготовления выбранных блюд согласно рецепта/ов.

### Технологии

- Python 3.7
- Django 4
- Django Rest Framework 3.14
- PostgreSQL 14.0-alpine
- Nginx 1.21.3-alpine

### Управление пользователями через API

- Регистрация пользователя администратором проекта;
- Самостоятельная регистрация пользователей;
- Передача подтверждающего кода пользователю по электронной почте;
- Присваивание токена пользователю для аутентификации;
- Изменение информации о пользователе;

## Документация
Подробное описание ресурсов доступно в документации после запуска проекта по адресу `http://localhost/api/docs/redoc.html`.

В документации указаны эндпоинты (адреса, по которым можно сделать запрос), разрешённые типы запросов, права доступа и дополнительные параметры (паджинация, поиск, фильтрация итд.), когда это необходимо.

# Структура проекта
- frontend - файлы, необходимые для сборки фронтенда приложения;
- infra - инфраструктура проекта: конфигурационный файл nginx и docker-compose.yml;
- backend - файлы, необходимые для сборки бэкенд приложения;
- data - подготовлен список ингредиентов с единицами измерения. Экспорт ингредиентов осуществляется командой ```python manage.py loaddata ingredients.json```

# Пользовательские роли
- Анонимный пользователь
- Аутентифицированный пользователь
- Администратор

### Анонимные пользователи могут:
- Просматривать список рецептов;
- Просматривать отдельные рецепты;
- Фильтровать рецепты по тегам;
- Создавать аккаунт

### Аутентифицированные пользователи могут:
- Получать данные о своей учетной записи;
- Изменять свой пароль;
- Просматривать, публиковать, удалять и редактировать свои рецепты;
- Добавлять понравившиеся рецепты в избранное и удалять из избранного;
- Добавлять рецепты в список покупок и удалять из списка;
- Подписываться и отписываться на авторов;
- Скачивать список покупок

## Запуск проекта на сервере (через Docker контейнеры)
VM (Ubuntu 22.04) для Docker Compose V2:

1. Остановите работу nginx, если он у вас установлен и запущен

```
sudo systemctl stop nginx
```

2. Установите последние обновления на виртуальную машину:

```
sudo apt update
sudo apt upgrade -y
```

3. Установите Docker Docker Compose V2

```
sudo apt install docker.io

sudo mkdir -p /usr/local/lib/docker/cli-plugins
sudo curl -SL https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-linux-x86_64 -o /usr/local/lib/docker/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
```

## Подготовка сервера для запуска проекта:

- Укажите публичный адрес вашего сервера в nginx.conf
```
server_name <ip вашего сервера>;
```
5. Скопируйте на сервер файлы docker-compose.yml, nginx.conf из папки infra-server (команды выполнять находясь в папке infra-server):
```
scp docker-compose.yml nginx.conf username@IP:/home/username/
```
6. Для работы с GitHub Actions и деплоя необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:
```
SECRET_KEY              # секретный ключ Django проекта
DOCKER_PASSWORD         # пароль от Docker Hub
DOCKER_USERNAME         # логин Docker Hub
HOST                    # публичный IP сервера
USER                    # имя пользователя на сервере
PASSPHRASE              # *если ssh-ключ защищен паролем
SSH_KEY                 # приватный ssh-ключ
TELEGRAM_TO             # ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          # токен бота, посылающего сообщение

DB_ENGINE               # django.db.backends.postgresql
DB_NAME                 # postgres
POSTGRES_USER           # postgres
POSTGRES_PASSWORD       # postgres
DB_HOST                 # db
DB_PORT                 # 5432 (порт по умолчанию)
```

7. После успешного запуска контейнеров выполните
```
sudo docker compose exec backend python manage.py makemigrations
sudo docker compose exec backend python manage.py migrate
sudo docker compose exec backend python manage.py createsuperuser
sudo docker compose exec backend python manage.py collectstatic --no-input
```

8. Выполните импорт ингредиентов:
```
sudo docker compose exec backend python manage.py loaddata ingredients.json
```

## Github Actions CI:
После каждого обновления репозитория (push в ветку master) будет происходить:
1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
2. Сборка и доставка докер-образов frontend и backend на Docker Hub
3. Разворачивание проекта на удаленном сервере
4. Отправка сообщения в Telegram в случае успеха

Сайт станет доступным для работы:

- Панель администратора: http://51.250.92.178/admin
- Главная страница сайта: http://51.250.92.178/recipes

## Автор
**Трушечкин Ростислав**
(https://github.com/Rostislaff/foodgram-project-react.git)