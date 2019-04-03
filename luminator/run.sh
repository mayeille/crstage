#!/bin/sh
source $HOME/venv/serveur/bin/activate
FLASK_APP=app.py FLASK_ENV=development flask run --host="0.0.0.0"
