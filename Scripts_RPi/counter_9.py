import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

#for 9
GPIO.output(14,GPIO.HIGH)
GPIO.output(15,GPIO.HIGH)
GPIO.output(21,GPIO.HIGH)
GPIO.output(20,GPIO.HIGH)
GPIO.output(16,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)

GPIO.output(18,GPIO.LOW)

print("number 9 on")
