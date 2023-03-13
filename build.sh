#!/bin/bash

# Build the project
echo "Update Pip..."
python3.9 -m pip install --upgrade pip

echo "Install requirements..."
pip install -r requirements.txt

echo "Collect static..."
python3.9 manage.py collectstatic

echo "Make migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
