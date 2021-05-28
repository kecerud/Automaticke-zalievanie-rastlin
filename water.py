import RPi.GPIO as GPIO
import datetime
import time

init = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def get_naposledy_zaliate():
    try:
        f = open("naposledy_zaliate.txt", "r")
        return f.readline()
    except:
        return "Nikdy!"

def get_status(pin = 8):
    GPIO.setup(pin, GPIO.IN)
    return GPIO.input(pin)

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)

def auto_water(delay = 5, pump_pin = 7, water_sensor_pin = 8):
    consecutive_water_count = 0
    init_output(pump_pin)
    print("Zapnute automaticke zalievanie. CTRL+C pre vypnutie.")
    try:
        while 1 and consecutive_water_count < 10:
            time.sleep(delay)
            wet = get_status(pin = water_sensor_pin) == 0
            if not wet:
                if consecutive_water_count < 5:
                    pump_on(pump_pin, 1)
                consecutive_water_count += 1
            else:
                consecutive_water_count = 0
    except KeyboardInterrupt:
        GPIO.cleanup()

def pump_on(pump_pin = 7, delay = 1):
    init_output(pump_pin)
    datum = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    f = open("naposledy_zaliate.txt", "w")
    f.write("Naposledy bola rastlina zaliata {}".format(datum))
    f.close()
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(2)
    GPIO.output(pump_pin, GPIO.HIGH)

def pump_off(pump_pin=7):
    init_output(pump_pin)
    GPIO.output(pump_pin,GPIO.HIGH)
