import Rpi.GPIO as GPIO

from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)

sleep(0.5)
GPIO.output(3,GPIO.HIGH)
sleep(0,5)
GPIO.output(GPIO.LOW)
