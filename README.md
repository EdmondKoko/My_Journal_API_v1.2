API включает в себя посты, комментарии, подписчиков и группы. Авторизация реализованна через JWT-токен.

Стек технологий
Python 3.9.4, Django 3.1+, Django REST Framework, SQLite3, Simple JWT, Django Filter.

Установка
Создайте виртуальное окружение:

python -m venv venv
Активируйте его:

source venv/Scripts/activate
Используйте pip, чтобы установить зависимости:

pip install -r requirements.txt
После создайте в корневой директории файл с названием ".env" и поместите в него:

SECRET_KEY=любой_секретный_ключ_на_ваш_выбор
DEBUG=False
ALLOWED_HOSTS=*
Не забудьте применить все миграции:

python manage.py migrate
И запускайте сервер:

python manage.py runserver
Вход
Создайте супер пользователя, обязательно укажите имя пользователя и пароль:

python manage.py createsuperuser
Отправьте POST-запрос, с именем пользователя и паролем на http://127.0.0.1:8000/api/v1/token/, чтобы получить токен. Пример:

curl -X POST -F "username=ваше_имя_пользователя" -F "password=ваш_пароль" http://127.0.0.1:8000/api/v1/token/
Документация
Чтобы открыть документацию, запустите сервер и перейдите по ссылке: http://127.0.0.1:8000/redoc/