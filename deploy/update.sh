#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/wolf_djangoapi'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput
supervisorctl restart one_off_fee_api

echo "DONE! :)"
