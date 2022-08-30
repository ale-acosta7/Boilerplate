# Boilerplate
Basic Django/React file structure, configuration, and boilerplate code for new web application projects.
Also includes bare bones implementation of Celery for asynchronous task queues.

## Getting Started
1. (Optional) Choose a new project name and update the following (brackets should not be included):
    * Rename the two files named "Boilerplate".
    * In 'settings.py', update the following lines:
        * Line 64: `ROOT_URLCONF = '[new project name].urls'`
        * Line 82: `WSGI_APPLICATION = '[new project name].wsgi.application'`
        * Line 83: `ASGI_APPLICATION = '[new project name].asgi.application'`
    * In 'manage.py', update the following line:
        * Line 9: `os.environ.setdefault('DJANGO_SETTINGS_MODULE', '[new project name].settings')`
    * In 'asgi.py', update the following line:
        * Line 17: `os.environ.setdefault('DJANGO_SETTINGS_MODULE', '[new project name].settings')`
    * In 'wsgi.py', update the following line:
        * Line 14: `os.environ.setdefault('DJANGO_SETTINGS_MODULE', '[new project name].settings')`
    * In 'celery.py', update the following lines:
        * Line 6: `os.environ.setdefault('DJANGO_SETTINGS_MODULE', '[new project name].settings')`
        * Line 8: `app = Celery('[new project name]', broker='redis://127.0.0.1:6379/0')`