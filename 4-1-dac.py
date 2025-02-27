import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def decimal2bin(val):
    return[int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        dig = input("Введите целое число от 0 до 255:")
        
        if dig.lower() == 'q':
            break

        try:
            value = int(dig)

            if value < 0:
                print("Число должно быть неотрицательным ")
                break
            elif value > 255:
                print("Число должно быть строго меньше 256") 
                break
            bin_val = decimal2bin(value)

            GPIO.output(dac, bin_val)

            volt = (3.3 * value) / 256

            print("Предполагаемое напряжение: {:.2f} B".format(volt))

        except ValueError:
            print("Введено не числовое значение или не целое число")
            break

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()     
    print("Завершение работы")
