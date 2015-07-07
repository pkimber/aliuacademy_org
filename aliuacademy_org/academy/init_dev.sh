#!/bin/bash
# exit immediately if a command exits with a nonzero exit status.
set -e
# treat unset variables as an error when substituting.
set -u

py.test -x
touch database/data.sqlite && rm database/data.sqlite
python manage.py migrate --noinput
python manage.py demo_data_login
python manage.py init_app_web
python manage.py runserver
