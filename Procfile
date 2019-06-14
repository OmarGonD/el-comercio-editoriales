web: python manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT settings.py 
web: gunicorn el_comercio_app.wsgi --log-file -