python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn  --worker-class gevent --certfile=origin.pem --keyfile=key.pem --bind 0.0.0.0:3500 escalade.wsgi:application