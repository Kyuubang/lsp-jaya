# make migrations
python manage.py makemigrations

# migrate
python manage.py migrate

# run gunicorn
gunicorn --config gunicorn-cfg.py core.wsgi