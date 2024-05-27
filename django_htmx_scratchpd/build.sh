#!/usr/bin/env bash
# exit on error

( 
    set -e
    set -x
    
    pwd
    ls

    pip install -r requirements.txt

    python manage.py collectstatic --no-input
    python manage.py migrate
)