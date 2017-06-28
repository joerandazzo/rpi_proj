#Day 7 Assignments
#Joe Randazzo

#Assignment 1

#imports
import time
import RPi.GPIO as GPIO

#setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
red = GPIO.PWM(17,40)
red.start(0)

green = GPIO.PWM(18, 40)
green.start(100)
button_sleep = .1

	
def button_one_callback(channel):
	print('Button 1 Pressed')
	for i in range(0,101,5):
		red.ChangeDutyCycle(i)
		time.sleep(button_sleep)
		
def button_two_callback(channel):
	print('Button 2 Pressed')
	for i in range(0,101,5):
		green.ChangeDutyCycle(100-i)
		time.sleep(button_sleep)

	
GPIO.add_event_detect(27, GPIO.RISING, button_one_callback)
GPIO.add_event_detect(22, GPIO.RISING, button_two_callback)


try:
	while True:
		test = input('')
					
except KeyboardInterrupt:
	red.stop()
	green.stop()
	GPIO.cleanup() #ctrl-c
	
	

	
	
	

