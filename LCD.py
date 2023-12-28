import machine
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=200000)

devices = i2c.scan()
if len(devices) == 0:
 print("No i2c device !")
else:
 print('i2c devices found:', len(devices))
for device in devices:
 print("At address: ", hex(device))