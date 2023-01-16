# API для Yatube

#### API включает в себя посты, комментарии, подписчиков и группы. Авторизация реализованна через JWT-токен.

## Технологии
Python, Django, Django REST Framework, SQLite3, Simple JWT, Django Filter.

## Установка
### Создайте виртуальное окружение:

python -m venv venv
### Активируйте его:

source venv/Scripts/activate
### Используйте pip, чтобы установить зависимости:

pip install -r requirements.txt
### Выполнить миграции:

python3 manage.py migrate
### Запустить проект:

python3 manage.py runserver
