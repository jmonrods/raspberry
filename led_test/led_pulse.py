import machine
import time
import math

led0 = machine.PWM(machine.Pin(0), freq=1000)
led1 = machine.PWM(machine.Pin(1), freq=1000)
led2 = machine.PWM(machine.Pin(2), freq=1000)


def pulse(led_i, t):
    for i in range(20):
        led_i.duty_u16(int(32768 - math.cos(i / 10 * math.pi) * 32768))
        time.sleep_ms(t)


led_list = [led0, led1, led2]


while True:
    for led in led_list:
        pulse(led, 50)

