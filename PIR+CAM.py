import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
camera=PiCamera()

import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
while True:
    i=GPIO.input(11)
    if i==0:
       #print 'NO INTRUDERs'
       GPIO.output(3, 0)
       #Turn OFF LED
       time.sleep(0.1)
    elif i==1:               #When output from motion sensor is HIGH
        #print 'Intruders detected'
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.stop_preview()
        GPIO.output(3, 1)  #Turn ON LED
        time.sleep(0.1)
