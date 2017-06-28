#LED Pinout Example
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
 
pins = [17, 18, 27, 22]

for i, pin in enumerate(pins):
	GPIO.setup(pin, GPIO.OUT)
	for j in range(i+1): 
		GPIO.output(pin,1)
		print('pin on ' + str(pin))
		time.sleep(0.5)
		GPIO.output(pin,0)
		print('pin off ' + str(pin))
		time.sleep(0.5)
		
GPIO.cleanup()
