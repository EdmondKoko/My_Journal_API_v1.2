![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=yellow)
![Django](https://img.shields.io/badge/Django-2.2.6-red?style=for-the-badge&logo=django&logoColor=blue)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![SQLite](https://img.shields.io/badge/SQLite-grey?style=for-the-badge&logo=postgresql&logoColor=yellow)

# My_Journal - социальная сеть для публикации личных дневников. 

## Описание:
### API для My_Journal.

В проекте реализовано:
- У неаутентифицированных пользователей доступ к API только на уровне чтения.
- Для эндпойнта /follow/ установлено дополнительное ограничение. Доступ к нему только у аутентифицированных пользователей.
- Аутентифицированным пользователям разрешено изменение и удаление своего контента, в остальных случаях доступ предоставляется только для чтения.
- Подписки на пользователей.
- Просмотр, создание, изменение и удаление записей.
- Просмотр и создание групп.
- Возможность добавления, редактирования, удаления своих комментариев и просмотр чужих.
- Фильтрация по полям.

### Запуск приложения:

Клонируем проект:

```bash
git clone https://github.com/edmondkoko/My_Journal_API_v1.2.git
```

Переходим в папку с проектом:

```bash
cd My_Journal_API_v1.2
```

Устанавливаем виртуальное окружение:

```bash
python3 -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/bin/activate
```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

Создаем супер пользователя:

```bash
python manage.py createsuperuser
```

Запускаем проект:

```bash
python manage.py runserver
```

После чего проект будет доступен по адресу (http://127.0.0.1:8000/)


### Примеры некоторых запросов API
Получить список всех постов:

```bash
GET /api/v1/posts/
```

Добавление нового поста:
```bash
POST /api/v1/posts/
```

Получить список всех групп:
```bash
GET /api/v1/groups/
```

Добавление нового комментария:
```bash
POST /api/v1/posts/{post_id}/comments/
```

Удаление комментария по id:
```bash
DELETE /api/v1/posts/{post_id}/comments/{id}/
```

Получение списока подписок:
```bash
GET /api/v1/follow/
```

Подписка пользователя на пользователя переданного в запросе:
```bash
POST /api/v1/follow/
```

Полный список запросов API находятся в документации
