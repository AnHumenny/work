# Aiogram3 bot Application


- **Python** (версия 3.11)
- **MySQL** (версия 15 или выше)
- **pip** 
- **virtualenv** (опционально)

## Установка

python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows

## Установите зависимости:
pip install -r requirements.txt

Настройте базу данных:
Создайте базу данных в MySQL(MariaDB) и обновите настройки в .env вашего проекта:

API_TOKEN = 'TOKEN'
host='host'
port="port"
user="user"
password="password"
database="database"

##Запуск бота
Чтобы запустить бота, выполните следующую команду:
python3 bot.py
python3 dynamic.py (мониторинг по времени(указывается))



