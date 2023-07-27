# Используйте базовый образ Python
FROM python:3.11

# Устанавливаем переменные окружения для Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем директорию для приложения
RUN mkdir /app
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем проект в контейнер
COPY . /app/

# Запускаем сервер разработки Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]