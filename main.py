from machine import Pin, I2C, ADC
from time import sleep, sleep_ms
from machine_i2c_lcd import I2cLcd

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
addr = i2c.scan()[0]
lcd = I2cLcd(i2c, addr, 2, 16)

lcd.putstr("Hola Illy!\n")
lcd.putstr("Ya funciona esto")
sleep(1)
