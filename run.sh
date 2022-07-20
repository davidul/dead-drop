#! /usr/bin/env sh

export FLASK_APP=dd-app
flask init-db

gunicorn -b 0.0.0.0:8080 'dd-app:create_app()'