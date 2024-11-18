# Aiogram3 bot Application

Приложение предназначено для обработки рабочей информации, хранящейся в БД приложения, а так же обновления и добавления новых заявок, отображения информации из БД в графиках. Использует PostgreSQL в качестве базы данных.

Перед тем как начать, убедитесь, что у вас установлены следующие компоненты:

- **Python** (версия 3.11)
- **PostgreSQL** (версия 14)
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

API_TOKEN = 'TOKEN'
host='host'
port="port"
user="user"
password="password"
database="database"

##Запуск приложения
Чтобы запустить приложение, выполните следующую команду:
python3 bot.py



