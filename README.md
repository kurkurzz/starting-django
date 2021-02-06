# Steps to start developing django project

This repo is created for my personal reference to create a restful api project using django. If you find it helpful then it's good.

### Setup project

1.  ```sh 
    pip install django djangorestframework markdown django-filter
    ```
2. Go to folder where you want the project to be and run:
    ```sh 
    django-admin startproject {project-name}
    ```
3. In `settings.py`, add
<br/>
    ```python
    INSTALLED_APPS = [
    ...
    'rest_framework',
    ]
    ```

### Create app

1. Go to the project directory and run:
    ```sh 
    python manage.py startapp {app-name}
    ```
2. In `settings.py` in the main app folder, add 
<br/>
    ```python
    INSTALLED_APPS = [
    ...
    '{app-name}.apps.ApiConfig',
    ]
    ```

3. In the app folder, create `urls.py` file.
4. In `urls.py` in the main app folder, add 
    ```python
    urlpatterns = [
    ...
    path('{name-of-the-slug}/', include('{app-name}.urls'))
    ]
    ```

### Basic Commands

-   Create project
    ```sh 
    django-admin startproject {project-name}
    ```
-   Run server
    ```sh 
    python manage.py runserver
    ```
-   Migrate data
    ```sh 
    python manage.py migrate
    ```
-   Create migration
    ```sh 
    python manage.py makemigrations
    ```
-   Create admin account
    ```sh 
    python manage.py createsuperuser
    ```

### Connect with MySQL Database

- In `settings.py` add this (rid the default one)
  ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'razaknews',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {
                'sql_mode': 'traditional',
            }
        }
    }
    ```

- In `Models.py`, make sure the models have the same attributes and types with the database.

- To migrate when the table already exist, run 
    ```sh
    python manage.py migrate --fake {table-name}
    ```
