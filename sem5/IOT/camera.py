from picamera import Picamera
from time import sleep

camera= Picamera()
camera.rotation=180

camera.start_preview()

for i in range(2):
    sleep(5)
    camera.capture('C:\Users\Ecourt\Desktop\ANIMATED\IMAGES%s.jpg'%i)

camera.stop_preview()