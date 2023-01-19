# API для Yatube

## Описание проекта:
#### Yatube - проект социальной сети. «API для Yatube» расширяет возможности социальной сети. Новый функционал позволяет пользователям публиковать свои посты и управлять подписками через программный интерфейс взаимодействия.
## Технологии
- Python - язык программирования.
- Django - свободный фреймворк для веб-приложений на языке Python.
- Django REST Framework - мощный и гибкий набор инструментов для создания веб-API.
- Simple JWT - плагин аутентификации JSON Web Token для Django REST Framework.

## Установка: 

### Клонировать репозиторий:

- git clone https://github.com/edmondkoko/api_final_yatube.git
### Создайте и активиркйте виртуальное окружение:

- python -m venv venv
- source venv/Scripts/activate
### Используйте pip, чтобы установить зависимости:

- pip install -r requirements.txt
### Выполнить миграции:

- python manage.py migrate
### Запустить проект:

-  python manage.py runserver

### После запуска проекта, документация будет доступна по адресу:
http://localhost:port/redoc/

### Примеры запросов:

#### POST-запрос с токеном, добавление новой публикации в коллекцию публикаций.

- POST http://localhost:port/api/v1/posts/

```
{
  "text": "Любой текст",
  "group": 1
}
```

#### Ответ

```
{
    "id": 1,
    "author": "User",
    "text": "Любой текст",
    "pub_date": "2015-03-04T00:00:00.000Z",
    "image": null,
    "group": 1
}
```
#### GET-запрос, получение информации о сообществе по id=2.

- GET http://localhost:port/api/v1/groups/2/

#### Ответ

```
{
    "id": 1
    "title": "group2",
    "slug": "group2",
    "description": "group2"
}
```

#### POST-запрос, подписка авторизованного пользователя от имени которого сделан запрос на автора интересующей публикации

- POST http://localhost:port/api/v1/follow/
```
{
  "following": "admin"
}
```
#### Ответ
```
{
    "id": 1,
    "user": "User",
    "following": "admin"
}
```