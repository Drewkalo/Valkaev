import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def decimal2bin(val):
    return[int(element) for element in bin(value)[2:].zfill(8)]

try:
    period = float(input("Введите период треугольного сигнала(в секундах)"))
    step = period / 512
    
    while True:
        for value in range(256):
            bin_val = decimal2bin(value)
            GPIO.output(dac, bin_val)
            time.sleep(step)

        for value in range(255, -1, -1):
            bin_val = decimal2bin(value)
            GPIO.output(dac, bin_val)
            time.sleep(step)

except ValueError:
    print("Ошибка: неверный ввод периода сигнала")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()