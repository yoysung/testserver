#!/usr/bin/env bash
# exit on error
set -o errexit

# Move to the Django project directory
cd djangoApp/gameCatalog

# Upgrade pip first
/opt/render/project/python/bin/python -m pip install --upgrade pip

# Then install requirements
pip install -r ../../requirements.txt

# Run Django commands
python manage.py collectstatic --noinput


