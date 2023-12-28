import machine
import time

# Led
led0 = machine.Pin(6, machine.Pin.OUT)
led1 = machine.Pin(7, machine.Pin.OUT)
led2 = machine.Pin(8, machine.Pin.OUT)
led3 = machine.Pin(9, machine.Pin.OUT)


led0.value(True)
led1.value(True)
led2.value(True)
led3.value(True)


# Frontal power
motorFR = machine.PWM(machine.Pin(0), freq=1000)
motorFL = machine.PWM(machine.Pin(1), freq=1000)

# Frontal right direction
directionFR0 = machine.Pin(2, machine.Pin.OUT)
directionFR1 = machine.Pin(3, machine.Pin.OUT)

# Frontal left direction
directionFL0 = machine.Pin(4, machine.Pin.OUT)
directionFL1 = machine.Pin(5, machine.Pin.OUT)

directions = [directionFR0, directionFR1, directionFL0, directionFL1]
motors = [motorFR, motorFL]


# Movement
def accelerate():
    motors[0].duty_u16(int(65536))
    motors[1].duty_u16(int(65536))


def stop():
    motors[0].duty_u16(int(0))
    motors[1].duty_u16(int(0))


# Directions
def left():
    directions[0].value(1)
    directions[1].value(0)

    directions[2].value(0)
    directions[3].value(1)


def right():
    directions[0].value(0)
    directions[1].value(1)

    directions[2].value(1)
    directions[3].value(0)


def forward():
    directions[0].value(0)
    directions[1].value(1)

    directions[2].value(0)
    directions[3].value(1)


def backwards():
    directions[0].value(1)
    directions[1].value(0)

    directions[2].value(1)
    directions[3].value(0)


while True:
    led0.toggle()
    led1.toggle()
    led2.toggle()
    led3.toggle()
    time.sleep(1)
    stop()
    forward()
    time.sleep(2)
    accelerate()
    time.sleep(2)
    left()
    time.sleep(2)
    forward()
    time.sleep(2)
    right()
    time.sleep(2)
    backwards()
    time.sleep(2)
    stop()

