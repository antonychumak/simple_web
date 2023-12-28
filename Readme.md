How to run:
If not venv:
    python3 -m venv venv
    source venv/bin/activate

pip install -r requirements.txt

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py loaddata web_fixture
4. python manage.py runserver
