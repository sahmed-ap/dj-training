# dj-training
The repo contains training session of python and django.

# virtual environment
Python virtual environments give you the ability to isolate your Python development projects from your system installed Python (like a separate sandbox) and other Python environments. 
This gives you full control of your project and makes it easily reproducible

# Create a virtual environment
# Windows
1. Run "python -m venv myvenv", where myvenv is the name of the virtual environment.
2. Go to scripts directory of the virtual environment
3. cd myvenv/Scripts
4. Run "activate" to activate virtual environment

# Mac OS
1. Run "python -m venv myvenv", where myvenv is the name of the virtual environment.
2. Go to scripts directory of the virtual environment
3. Run "source my_env/bin/activate" to activate virtual environment


After activating the virtual environment Run "pip install any-python-lib-that-needs-to-installed"


# Django
# Create a Django Project
1. Run "pip install django" after activating the virtual environment.
2. cd dir/where/django/project/needs/to/be/created
3. django-admin startproject project-name
4. Create django app as the project needs an app to be run "python manage.py startapp django-app-name"
5. Go to settings.py/base.py, add the app name in the "INSTALLED_APPS" list.
6. Check and update Database configurations in the "DATABASES" variable in settings.py/base.py.
7. Go to project root in terminal and run "python manage.py makemigrations", and then run "python manage.py migrate"
8. Run "python manage.py runserver" and hit "http://localhost:8000" to test if server is running successfully.


# Create superuser and view admin site
1. From project root run "python manage.py createsuperuser"
2. Enter super user credentials, as needed.
3. Run "python manage.py runserver" and hit "http://localhost:8000/admin"
4. Enter the superuser credentials created earlier.
5. Now you can view Database records and perform CRUD operations on them, moreover you can manage and manipulate user access control from users and groups.
