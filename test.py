import framebuf
import machine
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=200000)

print("IC2 address: " + hex(i2c.scan()[0]))

oled = SSD1306_I2C(128, 64, i2c)

inv1a = bytearray(b"\xd0xPx\xf0")
buffer = bytearray(eyes)
#fbuf = framebuf.FrameBuffer(buffer, 10, 6, framebuf.MONO_HLSB)
inv1aBuff = framebuf.FrameBuffer(inv1a, 7, 7, framebuf.MONO_HLSB)

oled.fill(0)
#oled.text("Hello", 0, 20)
oled.blit(inv1aBuff, 7, 7)
oled.show()

