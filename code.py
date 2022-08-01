print("Hello World!")
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""

import board
import terminalio
import displayio
import digitalio
import pwmio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

from adafruit_slideshow import PlayBackOrder, SlideShow

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.CS
tft_dc = board.D1

display_bus = displayio.FourWire(
	spi, command=tft_dc, chip_select=tft_cs, reset=board.D0
)

display = ST7735R(display_bus, width=128, height=160, rotation=0, bgr=True, colstart=2, rowstart=1)

# bl = digitalio.DigitalInOut(board.PWM0)
# bl.direction = digitalio.Direction.OUTPUT
# bl.value = True

bl = pwmio.PWMOut(board.PWM0, frequency=5000, duty_cycle=0)
bl.duty_cycle = 60000

# Make the display context
splash = displayio.Group()
display.show(splash)


color_bitmap = displayio.Bitmap(128, 160, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000  # Bright Red

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(118, 150, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xFFFFFF # White
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=5)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(scale=2, x=11, y=64)
text = "BornHack"
text_area = label.Label(terminalio.FONT, text=text, color=0x000000)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)



# Create the slideshow object that plays through once alphabetically.
slideshow = SlideShow(display,
                      folder="/images",
                      loop=True,
                      order=PlayBackOrder.ALPHABETICAL,
                      dwell=60)

while slideshow.update():
    pass


while True:
	pass
