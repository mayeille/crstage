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
	if value:
		v = 1
	else:
		v = 0

	mb = arduino_connect()
	try:					
		mb.write_registers(ADDRESS_LED, [v])
	except Exception as e:
		print(e)
	mb.close()

def arduino_read_led():
	mb = arduino_connect()
	read_data = mb.read_registers(ADDRESS_LED, 1)
	mb.close()
	print(list(read_data))
	return bool(read_data[0])


def arduino_connect(): 
	mb = pylibmodbus.ModbusRtu(device="/dev/ttyACM0", baud=115200)
	mb.set_slave(1)
	mb.connect()
	return mb
