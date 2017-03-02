import time
from RPi import GPIO
pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
while True:
    inputval = GPIO.input(pin)
    print ("VALUE: {}".format(inputval))
    time.sleep(0.05)