import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 23
LED = 24

GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

while True:
	button_state = GPIO.input(button)
	if button_state == 0:
		GPIO.output(LED,GPIO.HIGH)
		print "LED ON"
	else:
		GPIO.output(LED,GPIO.LOW)
		print "LED OFF"
	time.sleep(1)
GPIO.cleanup()
