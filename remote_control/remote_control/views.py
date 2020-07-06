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

		# ========= Front wheel cali ===========
		elif action == 'fwcali':
			print('"%s" command received' % action)
			fw.calibration()
		elif action == 'fwcalileft':
			print('"%s" command received' % action)
			fw.cali_left()
		elif action == 'fwcaliright':
			print('"%s" command received' % action)
			fw.cali_right()
		elif action == 'fwcaliok':
			print('"%s" command received' % action)
			fw.cali_ok()

		# ========= Back wheel cali ===========
		elif action == 'bwcali':
			print('"%s" command received' % action)
			bw.calibration()
		elif action == 'bwcalileft':
			print('"%s" command received' % action)
			bw.cali_left()
		elif action == 'bwcaliright':
			print('"%s" command received' % action)
			bw.cali_right()
		elif action == 'bwcaliok':
			print('"%s" command received' % action)
			bw.cali_ok()
		else:
			print('command error, error command "%s" received' % action)
	return render_to_response("cali.html")

def connection_test(request):
	return HttpResponse('OK')
