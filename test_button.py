import time
from RPi import GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
while True:
    	inputval = GPIO.input(pin)
    	print ("STATUS: 25: {} 24: {} 23: {} 18: {} 15: {} 14: {}".format(GPIO.input(25), GPIO.input(24), GPIO.input(23), GPIO.input(18), GPIO.input(15), GPIO.input(14))
    	time.sleep(0.05)