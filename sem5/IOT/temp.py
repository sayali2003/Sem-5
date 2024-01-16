import RPi.GPIO as GPIO
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)
while True:
    humidity, temperature= Adafruit_DHT.read_retry(Adafruit_DHT11,2)
    print (humidity, temperature)
GPIO.cleanup()