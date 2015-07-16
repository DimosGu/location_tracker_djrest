# location_tracker_djrest
Event based location tracker Rest API which was developed with Django Rest Framework (+Haystack)

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

# collect static
    python manage.py collectstatic

# .gitignore file

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

# heroku deployment
    1- heroku login
    2- heroku create
    3- git push heroku master
    4- heroku run python manage.py syncdb
    5- heroku ps:scale web=1
    6- heroku open

# Elastic Search installation and configuration (Haystack)
    1- ES required java 1.7+
    2- brew install Caskroom/cask/java
    3- install: brew install elasticsearch
    4- start: elasticsearch -f -D es.config=/usr/local/Cellar/elasticsearch/1.4.2/config/elasticsearch.yml
    5- pip install django-haystack and add to requirements.txt
    6- add HAYSTACK_CONNECTIONS to to settings.py
    7- add search_indexes.py and add SearchIndex classes
    8- pip install elasticsearch and add to requirements.txt
    9- python manage.py rebuild_index
    10- override retrieve url of model view set adding search ability

# Search integration on Heroku (Elastic Search)
    1- https://devcenter.heroku.com/articles/searchbox#using-haystack-with-django

# Elastic search REST usage
    1- get all documents: http://localhost:9200/haystack_djrest/_search?q=*&pretty
    2- delete index: DELETE http://localhost:9200/haystack_djrest/