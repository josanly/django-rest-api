release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py createsuperuser --no-input --username admin
release: python manage.py changepassword admin

web: gunicorn django_rest_api.wsgi
