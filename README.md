python manage.py makemigrations <app_name>
python manage.py migrate

# if you delete migrations folder, you can apply syncdb. If not , you should use migrations command to create custom tables

http://localhost:5001/api/v1/events/

[
    {
        "plate": "34eb955",
        "msisdn": "+41524204242",
        "location": "35.479,58.683",
        "created_at": "2015-07-11T14:08:22.814584Z"
    },
    {
        "plate": "34eb955",
        "msisdn": "+41524204242",
        "location": "35.479,58.683",
        "created_at": "2015-07-11T14:08:23.704971Z"
    }
]


POST : add header Content-Type: application/json
url: http://localhost:5001/api/v1/events/
data: {
  "location": "35.456,58.678",
  "msisdn": "+41524204242",
  "plate": "34eb955"
}

# to enable pagination
 add REST_FRAMEWORK = {'PAGE_SIZE': 10} to settings.py