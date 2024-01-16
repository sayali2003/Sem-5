import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.out)
GPIO.setup(3, GPIO.out)
while True:
  var=GPIO.input()
  print(var)

if var==0:
  GPIO.output(3, True)
else:
  GPIO.output(3,False)
GPIO.cleanup()
