#!/usr/bin/env bash

python manage.py collectstatic --noinput
./scripts/db_health_check.sh
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000
