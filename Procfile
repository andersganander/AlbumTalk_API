release: python manage.py makemigrations && python manage.py migrate

web: gunicorn AlbumTalk_API.wsgi
