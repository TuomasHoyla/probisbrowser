Initial requirements:
Python 2.7 (3.x should work ok)
pip
virtualenv is also recommended (makes stuff easier), see http://docs.python-guide.org/en/latest/dev/virtualenvs/

Run:
#pip install -r requirements.txt

Migrations:

#python manage.py migrate

and after that on project folder

#python manage.py runserver

if no errors, head to 127.0.0.1:8000 with your browser
