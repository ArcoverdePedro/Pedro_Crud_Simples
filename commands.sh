#!/bin/sh
python manage.py collectstatic --noinput

python manage.py makemigrations --noinput

python manage.py migrate 

granian --interface wsgi projeto.wsgi:application --host 0.0.0.0 --port 8002 --interface wsgi --workers 5  --blocking-threads 2 --workers-lifetime 3900 --workers-max-rss 1000 --respawn-interval 100
