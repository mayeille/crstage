#!/bin/sh
source $HOME/venv/serveur/bin/activate
FLASK_APP=hello.py FLASK_ENV=development flask run
