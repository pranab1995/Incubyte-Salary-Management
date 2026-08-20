#!/bin/bash
set -e

echo "Waiting for postgres..."
# simple wait logic can be added here if needed

echo "Apply database migrations"
python manage.py migrate

echo "Starting server"
exec "$@"
