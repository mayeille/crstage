# coding: utf-8
from flask import Flask
app = Flask(__name__)

led_on = False

@app.route('/')
def hello_world():
	return 'quel est votre nom ?'

@app.route('/led/')
def led():
    if led_on:
        return "Allumée"
    else:
        return "Éteinte"
	

@app.route('/led/', methods=['GET', 'POST'])
def led():
    if led_on:
        return "Alumée"
    else
        return "Éteinte"
    
def login():
    if request.method == 'POST':
        return
    else:
        return
