# coding: utf-8
from flask import Flask, request, render_template
app = Flask(__name__)

led_on = True

def set_led(request):
	global led_on
	if "light" not in request.form:
		return "light argument is missing", 400

	if request.form["light"] == "on":
		led_on = True
	else:
		led_on = False	

@app.route('/', methods=['GET', 'POST'])    
def led():
	if request.method == 'POST':
		set_led(request)
	
	return render_template('pageled.html', led_on=led_on)
	
		

