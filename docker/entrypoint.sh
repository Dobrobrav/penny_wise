#!/bin/sh

echo "Waiting for postgres..."

max_retries=15
attempt=1

while ! nc -z db 5432; do
  if [ $attempt -ge $max_retries ]; then
    echo "Postgres is still not available after $max_retries attempts. Exiting."
    exit 1
  fi
  echo "Postgres not available yet (attempt $attempt/$max_retries)..."
  attempt=$((attempt + 1))
  sleep 1
done

echo "Postgres is up - executing commands"

python manage.py migrate
python manage.py runserver 0.0.0.0:80
