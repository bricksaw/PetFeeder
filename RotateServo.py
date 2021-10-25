# rotate servo
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(0)


##p.ChangeDutyCycle(12.5)  # turn towards 90 degree
##time.sleep(.16) # sleep 1 second
p.ChangeDutyCycle(12.5)  # turn towards 90 degree
time.sleep(.25) # sleep 1 second

p.ChangeDutyCycle(2.5)  # turn towards 90 degree
time.sleep(.5) # sleep 1 second


p.stop()
GPIO.cleanup()