import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
while True:
    var=GPIO.input(5)
    print(var)

    if var==1:
        GPIO.output(3, True)
    else:
        GPIO.output(3, False)
GPIO.cleanup()