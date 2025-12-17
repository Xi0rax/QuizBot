# Используем официальный Python образ
FROM python:3.11-slim

# Отключаем буферизацию логов
ENV PYTHONUNBUFFERED=1

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Запуск бота
CMD ["python", "main.py"]
