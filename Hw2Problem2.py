#Hw2 Problem 2
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
pins = [17, 27, 22, 18]

switch = False;
try:
	for i in range(5):
		for pin in pins: 
			GPIO.output(pin,0)
			time.sleep(0.13)
			GPIO.output(pin,1)
			time.sleep(0.13)
			GPIO.output(pin,0)
			
		for pin in reversed(pins): 
			GPIO.output(pin,0)
			time.sleep(0.13)
			GPIO.output(pin,1)
			time.sleep(0.13)
			GPIO.output(pin,0)	
			
	GPIO.cleanup()
except KeyboardInterrupt:
	GPIO.cleanup() #ctrl-c

