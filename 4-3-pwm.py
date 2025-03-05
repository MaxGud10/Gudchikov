import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)

n = 10
p = GPIO.PWM(10, 1000)
p.start(0)

try:
    while True:
        a = int(input())
        p.ChangeDutyCycle(a)
        print(3.3 *a/100)

finally:
    p.stop()
    GPIO.output(10, 0)
    GPIO.cleanup()
