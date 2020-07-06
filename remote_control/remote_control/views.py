'''
**********************************************************************
* Filename    : views
* Description : views for server
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-09-13    New release
**********************************************************************
'''

from django.shortcuts import render_to_response
from .driver import camera, stream
from picar import back_wheels, front_wheels
from django.http import HttpResponse
import picar

picar.setup()
db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"
fw = front_wheels.Front_Wheels(debug=False, db=db_file)
bw = back_wheels.Back_Wheels(debug=False, db=db_file)
cam = camera.Camera(debug=False, db=db_file)
cam.ready()
bw.ready()
fw.ready()
 
SPEED = 60
bw_status = 0

print(stream.start())

def home(request):
	return render_to_response("base.html")

def run(request):
	global SPEED, bw_status
	debug = ''
	if 'action' in request.GET:
		action = request.GET['action']
		
		
		# ================ Camera =================
		elif action == 'camready':
			cam.ready()
		elif action == "camleft":
			cam.turn_left(40)
		elif action == 'camright':
			cam.turn_right(40)
		elif action == 'camup':
			cam.turn_up(20)
		elif action == 'camdown':
			cam.turn_down(20)	
	if 'speed' in request.GET:
		speed = int(request.GET['speed'])
		if speed < 0:
			speed = 0
		if speed > 100:
			speed = 100
		SPEED = speed
		if bw_status != 0:
			bw.speed = SPEED
		debug = "speed =", speed
	host = stream.get_host().decode('utf-8').split(' ')[0]
	return render_to_response("run.html", {'host': host})

def cali(request):
	if 'action' in request.GET:
		action = request.GET['action']
		# ========== Camera calibration =========
		if action == 'camcali':
			print('"%s" command received' % action)
			cam.calibration()
		elif action == 'camcaliup':
			print('"%s" command received' % action)
			cam.cali_up()
		elif action == 'camcalidown':
			print('"%s" command received' % action)
			cam.cali_down()
		elif action == 'camcalileft':
			print('"%s" command received' % action)
			cam.cali_left()
		elif action == 'camcaliright':
			print('"%s" command received' % action)
			cam.cali_right()
		elif action == 'camcaliok':
			print('"%s" command received' % action)
			cam.cali_ok()

	

def connection_test(request):
	return HttpResponse('OK')
