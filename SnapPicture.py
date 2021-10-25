# take a picture
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(1):
    sleep(5)
     
    import datetime
    import time
    camera.resolution = (800, 600)
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    camera.capture("/var/www/html/images/CatFeeder_"+ date + ".jpg")
    camera.capture("/var/www/html/images/CatFeeder_Latest.jpg")
    
camera.stop_preview()