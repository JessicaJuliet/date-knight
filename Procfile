release: python manage.py collectstatic --noinput; python manage.py makemigrations; python manage.py migrate
web: gunicorn date_knight.wsgi --log-file -