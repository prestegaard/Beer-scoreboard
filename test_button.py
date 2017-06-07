from time import sleep
from RPi import GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(14, GPIO.IN)
while True:
	print ("STATUS: 25: {} 24: {} 23: {} 18: {} 15: {} 14: {}".format(str(GPIO.input(25)), str(GPIO.input(24)), str(GPIO.input(23)), str(GPIO.input(18)), str(GPIO.input(15)), str(GPIO.input(14))))
	sleep(0.05)
