python manage.py migrate
gunicorn django_pod.wsgi -c config.py