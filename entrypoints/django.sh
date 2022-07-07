#!/bin/bash -x
echo "Django shell script is running ..."

python manage.py collectstatic --noinput --settings=flight_tracking.settings &&
#python manage.py makemigrations  &&
python manage.py migrate --noinput --settings=flight_tracking.settings  &&
python manage.py runserver 0.0.0.0:8000 --settings=flight_tracking.settings  &&

gunicorn flight_tracking.wsgi:application --bind 0.0.0.0:8000

exec "$@"