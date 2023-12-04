#!/bin/bash

echo "Run back"
sleep 3

python manage.py loaddata /my_proj/db.json
python manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'Pasha13244')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000 --insecure
