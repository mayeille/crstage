# coding: utf-8
from flask import Flask, request, render_template
app = Flask(__name__)

led_on = True

def set_led(request):
	global led_on
	if "light" not in request.json:
		return "ligth argument is missing", 400

	if request.json["light"] == "on":
		led_on = True
	else:
		led_on = False

	return "LED status: %d" % led_on, 201

def get_led():
	global led_on
	return render_template('pageled.html', led_on=led_on)

@app.route('/', methods=['GET', 'POST'])    
def led():
	if request.method == 'POST':
		return set_led(request)
	else:
		return get_led()

