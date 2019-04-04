# coding: utf-8
from flask import Flask, request, render_template
import pylibmodbus

app = Flask(__name__)

ADDRESS_LED = 0

def set_led(request):
	if "light" not in request.form:
		return "light argument is missing", 400

	if request.form["light"] == "on":
		arduino_write_led(True)
	else:
		arduino_write_led(False)	

@app.route('/', methods=['GET', 'POST'])    
def led():
	if request.method == 'POST':
		set_led(request)
	
	led_on = arduino_read_led()
	return render_template('pageled.html', led_on=led_on)

def	arduino_write_led(value):
	global mb
	if value:
		v = 1
	else:
		v = 0

	mb.write_register(ADDRESS_LED, v)

def arduino_read_led():
	global mb
	read_data = mb.read_registers(ADDRESS_LED, 1)
	return bool(read_data[0])


mb = pylibmodbus.ModbusTcp("127.0.0.1", 1502)
mb.connect()
# mb.close()
