import time

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(60, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Clear all the pixels to turn them off.
pixels.clear()
pixels.show()  # Make sure to call show() after changing any pixels!

try:
    for minute in range(60):
        for second in range(60):
            if second < minute:
                pixels.set_pixel_rgb(second, 0, 0, 255)
            else:
                pixels.set_pixel_rgb(second, 255, 0, 0)
            pixels.show()
            time.sleep(1)
        pixels.clear()
        for m in range(minute + 1):
            pixels.set_pixel_rgb(m, 0, 0, 64)
        pixels.show()
except KeyboardInterrupt:
    pixels.clear()
    pixels.show()
