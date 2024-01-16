import machine
import time

led0 = machine.Pin(0, machine.Pin.OUT)
led1 = machine.Pin(1, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)

led0.value(False)
led1.value(False)
led2.value(False)

led_list = [led0, led1, led2]

while True:
    for led in led_list:
        led.toggle()
        time.sleep(1)
        led.toggle()

