# Используем официальный образ Python
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /bot_service

# Копируем файл зависимостей
COPY requirements.txt .

# Копируем весь код бота в контейнер
COPY . .

# Команда для запуска бота
CMD ["python3", "app.py"]
