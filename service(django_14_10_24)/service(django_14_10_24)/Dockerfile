FROM python:3.11

WORKDIR /service

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /service/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /service/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
