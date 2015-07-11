# location_tracker_djrest
Event based location tracker Rest API which was developed with Django Tastypie (+Haystack)

# Start project and app
    1- mkvirtualenv location_tracker_djrest
    2- workon location_tracker_djrest
    3- pip install django==1.8.1
    4- django-admin startproject location_tracker_djrest
    5- django-admin startapp app

# settings and wsgi
    1- db configuration
    2- ON_HEROKU check and add heroku db configuration (if will be deployed on heroku as well)
    2- add static serve configuration
    3- pagination configuration (django-rest framework) add REST_FRAMEWORK = {'PAGE_SIZE': 10} to settings.py
    4- add white-noise wsgi configuration

# Proc file, .env and runtime.txt
    1- Proc: web: gunicorn location_tracker_djrest.wsgi --log-file - (-b 0.0.0.0:<port> for binding)
    2- Proc.windows: web: python manage.py runserver 0.0.0.0:5000 (for windows)
    3- .env: DATABASE_URL=postgres:///location_tracker
    4- runtime.txt: python-2.7.9 (for heroku)

# requirements
    1- dj-database-url
    2- django
    3- djangorestframework
    4- django-postgrespool
    5- gunicorn
    6- psycopg2
    7- whitenoise
    8- SQLAlchemy
    9- django-phonenumber-field
    10- django-geposition
    * pip install -r requirements.txt

# models,syncdb and migrations
    1- add models
    2- remove migrations and run python manage.py syncdb (or try 3)
    3- keep migrations and;
        3.1- python manage.py makemigrations app
        3.2- python manage.py migrate

# run application
    1- foreman start web

# check application via postman
    1- get: http://localhost:5001/api/v1/events/
    2- post:
        2.1- add header: Content-Type application/json
        2.2- post data:{"location": "35.456,58.678","msisdn": "+41524204242","plate": "34eb955"}