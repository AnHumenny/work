# Tkinter Application

Приложение предназначено для обработки рабочей информации, хранящейся в БД приложения. Использует MySQL в качестве базы данных.

Перед тем как начать, убедитесь, что у вас установлены следующие компоненты:

- **Python** (версия 3.11)
- **MySQL** (версия 15)
- **pip** 
- **virtualenv** (опционально)

## Установка

python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows

## Установите зависимости:
pip install -r requirements.txt

Настройте базу данных:
Создайте базу данных в MySQL и обновите настройки в .env вашего проекта:

database_url = "mysql+asyncmy://user:password@host/database"

##Запуск приложения
Чтобы запустить приложение, выполните следующую команду:
python3 main.py


