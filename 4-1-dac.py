import RPi.GPIO as GPIO

def dec2bin(num):
    return [(num >> i) & 1 for i in range(7, -1, -1)]

GPIO.setwarnings(False)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

V_REF = 3.3  # Силка питания (может быть другой, проверьте на своем оборудовании)
MAX_DIGITAL_VALUE = 255  # Максимальное цифровое значение

try:
    while True:
        num = input("Введите целое число от 0 до 255 (или 'q' для выхода): ")
        try:
            if num == "q":
                break

            num = int(num)
            if 0 <= num <= MAX_DIGITAL_VALUE:
                GPIO.output(dac, dec2bin(num))
                voltage = (num / MAX_DIGITAL_VALUE) * V_REF  # Вычисляем выходное напряжение
                print(f"Выходное напряжение примерно {voltage:.4f} вольт")
            else:
                if num < 0:
                    print("Число должно быть >= 0")
                elif num > 255:
                    print("Число вне промежутка [0, 255]")
        except ValueError:
            print("Должно быть целое число < не строка или число с плавающей точкой")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")
# import RPi.GPIO as GPIO

# def dec2bin(num):
#     return [(num >> i) & 1 for i in range (7, -1, -1)]

# GPIO.setwarnings(False)
# dac = [8, 11, 7,1,0,5,12,6]
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(dac, GPIO.OUT)

# try:
#     while True:
#         num = input("Введите целое число от 0 до 255: ")
#         try:
#             num = int(num)
#             if 0 <= num <= 255:
#                 GPIO.output(dac, dec2bin(num))
#                 voltage = float(num)
#                 print(f"Output voltage is about {voltage:.4} volt")
#             else:
#                 if num < 0:
#                     print("Число должно быть >=0")
#                 elif num > 255:
#                     print("Число вне промежутка [0,255]")
#         except Exception:
#             if num == "q": break
#             print("Должно быть целое число < не строка или число с плавающей точкой")
# finally:
#     GPIO.output(dac, 0)
#     GPIO.cleanup()
#     print("EOP")