# Django Shop Application

Приложение предназначено для управления пользователями и заказами в интернет-магазине. Оно предоставляет API для работы с пользователями и заказами, а также использует PostgreSQL в качестве базы данных.


Перед тем как начать, убедитесь, что у вас установлены следующие компоненты:

- **Python** (версия 3.11)
- **PostgreSQL** (версия 14 или выше)
- **pip** 
- **virtualenv** (опционально)

## Установка

python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows

## Установите зависимости:
pip install -r requirements.txt

Настройте базу данных:
Создайте базу данных в PostgreSQL и обновите настройки в settings.py вашего проекта:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

##Примените миграции:
python manage.py migrate

##Запуск приложения
Чтобы запустить приложение, выполните следующую команду:
python manage.py runserver




