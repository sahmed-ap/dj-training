# Django -- The Practical Guide

This repository holds material of python django training.

### Course Content

- **Python Basics**
    - Variable declaration, Data Types and Type Conversion.
    - Loops, methods and decorators
    - File handling
    - object-oriented programming basic.

- **Django Framework**
  - Virtual env for django project.
  - Setup and understand django folder structure.
  - URLs, Routes and Views.
  - Templates and static files.
  - Data, models and relationships.
  - Forms and ORM.
  - Type of Views (Function Views, Class based Views)
  - Django Admin overview.

---------
### What is Virtual Env and How to create it.

#### virtual environment
Python virtual environments give you the ability to isolate your Python development projects from your system installed Python (like a separate sandbox) and other Python environments. 
This gives you full control of your project and makes it easily reproducible

#### Create a virtual environment
##### Windows
1. Run 
```
python -m venv myvenv
```
where myvenv is the name of the virtual environment.

2. Go to scripts directory of the virtual environment
```
cd myvenv/Scripts
```
3. Run 
```
activate
```
to activate virtual environment

After activating the virtual environment Run
```
pip install any-python-lib-that-needs-to-installed
```

##### Mac OS
1. Run 
```
python -m venv myvenv
```
where myvenv is the name of the virtual environment.

2. Run
```
source my_env/bin/activate
```
to activate virtual environment


After activating the virtual environment Run
```
pip install any-python-lib-that-needs-to-installed
```

# Django

### Create a Django Project
1. Run 
```
pip install django
```
after activating the virtual environment.

2. cd dir/where/django/project/needs/to/be/created
3. Run 
```
django-admin startproject project-name
```
4. Create django app as the project needs an app to be run
```
python manage.py startapp django-app-name
```

5. Go to settings.py/base.py, add the app name in the "INSTALLED_APPS" list.
6. Check and update Database configurations in the "DATABASES" variable in settings.py/base.py.
7. Go to project root in terminal and run "python manage.py makemigrations", and then run "python manage.py migrate"
8. Run "python manage.py runserver" and hit
```
http://localhost:8000
```
to test if server is running successfully.


## Create superuser and view admin site
1. From project root run
```
python manage.py createsuperuser
```

2. Enter super user credentials, as needed.
3. Run
```
python manage.py runserver
```

hit "http://localhost:8000/admin" from browser.

4. Enter the superuser credentials created earlier.
5. Now you can view Database records and perform CRUD operations on them, moreover you can manage and manipulate user access control from users and groups.

### Django URLs and Views Topics

- Adding a new url.
- Redirecting url.
- dynamic path segments url.
- reverse method use for URLs.

### Django Templates Topics

- Adding and setup templates.
- Rendering a templates through view.
- Passing variables to template from view.
- Template filters
- Template Tag - For tag | If tag etc
- Dynamic url tag
- Templates inheritance.
- Templates include.
- Adding static files (CSS) and settings.