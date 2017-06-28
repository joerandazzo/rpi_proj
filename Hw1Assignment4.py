#LED Pinout Text Input Handling 
import time
import RPi.GPIO as GPIO

#setup pins
GPIO.setmode(GPIO.BCM)
pins = [17, 18, 27, 22]
for i, pin in enumerate(pins):
	GPIO.setup(pin, GPIO.OUT)

#Listen for input
while 1:
	led_position = input('Enter LED Position: ')
	
	#Turn off pins
	for i, pin in enumerate(pins):
		GPIO.output(pin, 0)
	
	#Condition for pins
	if led_position == 1:
		GPIO.output(17,1)
	elif led_position == 2:
		GPIO.output(17,1)
		GPIO.output(27,1)
	elif led_position == 3:
		GPIO.output(17,1)
		GPIO.output(27,1)
		GPIO.output(22,1)
	else:
		print('Invalid position')
		
		
	#Clean up
	if led_position == 911:
		GPIO.cleanup()
		break;	
	



