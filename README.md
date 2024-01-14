# raspberry pi pico
Repository for testing the raspberry pi pico and peripherals

## references
* [Geeekpi GitHub repo](https://github.com/geeekpi/picokitadv)
* [Geeekpi Video tutorials](https://www.youtube.com/watch?v=YVWAyn7TJFk)
* [Geeekpi Wiki](https://wiki.52pi.com/index.php?title=K-0586)



# Raspberry Pi Pico WH

## References
* [Geeekpi Github repo](https://github.com/geeekpi/RPi_Pico_WH_IoT_Starter_kit)
* [Geeekpi Wiki] (https://wiki.52pi.com/index.php?title=KR-0006)


# Waveshare important links
* [waveshare LCD 240x280](https://www.waveshare.com/catalog/product/view/id/5540/s/1.69inch-lcd-module/category/335/)
* [Display examples](https://penfold.owt.com/st7789py/examples_tdisplay.html#ttgo-tdisplay-hello-py)
* [MicroPython ST7789V LCD Display](https://www.coderdojotc.org/micropython/displays/graph/14-lcd-st7789V/)

SPI Device pinout in Pico:
PIN | GP Number | Label on LCD | Description | SPI 
--- | --- | --- | --- | ---
14 | (GP10) | BL | BACKLIGHT PIN | SPI1 SCK
15 | (GP11)	| RST | RESET PIN | SPI1 TX
16 | (GP12)	| DC | DC PIN | SPI1 RX
17 | (GP13)	| CS | CS PIN | SPI1 CSn
-- | (GND)	| GND | GROUND | --
-- | (VCC)	| 3V3 | 3V3 (OUT) | --
19 | (GP14)	| CLK | CLK PIN | SPI1 SCK
20 | (GP15) | DIN | DIN PIN | SPI1 TX