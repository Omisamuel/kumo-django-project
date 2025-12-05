FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY requirements-prod.txt .
RUN pip install --no-cache-dir -r requirements.txt -r requirements-prod.txt

COPY . .

CMD bash -c "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn Kumo.wsgi:application --bind 0.0.0.0:8000"
