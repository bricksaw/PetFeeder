
exec(open("/home/pi/Desktop/PetFeeder/RotateServo.py").read())

from time import sleep
sleep(5)

exec(open("/home/pi/Desktop/PetFeeder/SnapPicture.py").read())

from time import sleep
sleep(5)

exec(open("/home/pi/Desktop/PetFeeder/SendEmail.py").read())