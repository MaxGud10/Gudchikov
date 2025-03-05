import RPi.GPIO as GPIO
from time import sleep
from matplotlib import pyplot as plt
import numpy as np

def dec2bin(num):
    return [(num >> i) & 1 for i in range(7, -1, -1)]

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

inc_flag = 1
t = 0
x = 0

try:
    period = float(input("Введите период: "))

    while True:
        GPIO.output(dac, dec2bin(x))

        if x == 0: 
            inc_flag = 1
        elif x == 255:
            inc_flag = 0
        
        x = x + 1 if inc_flag == 1 else x - 1

        print(x)
        sleep(period / 512)
        t += 1
except ValueError:
    print("Неподходящий период")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")