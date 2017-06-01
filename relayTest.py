import RPi.GPIO as GPIO
import time

print ("Setting")
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

print "Testing Relay Module Control with GPIO"

for i in range(2, 6):
    GPIO.output(i,True)
    time.sleep(1)
    print("GPIO %d is True" % (i))

for i in range(2, 6):
    GPIO.output(i,False)
    time.sleep(1)
    print("GPIO %d is False" % (i))
    
GPIO.cleanup()
