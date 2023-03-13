#!/bin/bash

# Build the project
echo "Building the project..."
pipenv shell
pipenv install

echo "Make migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect static..."
python manage.py collectstatic --noinput --clear
