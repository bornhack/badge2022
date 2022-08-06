import time
print("Hello BornHack!")
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""

import os

import board
import terminalio
import displayio
import digitalio
import pwmio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

from adafruit_slideshow import PlayBackOrder, SlideShow

def join(*xs):
    return '/'.join(x.rstrip('/') for x in xs)


def isfile(path):
    try:
        with open(path):
            pass
    except FileNotFoundError:
        return False
    else:
        return True

BTN_A = digitalio.DigitalInOut(board.BTN_A)
BTN_A.switch_to_input(pull=digitalio.Pull.UP)

BTN_B = digitalio.DigitalInOut(board.BTN_B)
BTN_B.switch_to_input(pull=digitalio.Pull.UP)

BTN_X = digitalio.DigitalInOut(board.BTN_X)
BTN_X.switch_to_input(pull=digitalio.Pull.UP)

BTN_Y = digitalio.DigitalInOut(board.BTN_Y)
BTN_Y.switch_to_input(pull=digitalio.Pull.UP)

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

def DrawMenu(currentselected, paths):
    rim_bitmap = displayio.Bitmap(128, 160, 1)
    rim_palette = displayio.Palette(1)
    rim_palette[0] = 0x000000 #black
    rim_sprite = displayio.TileGrid(rim_bitmap, pixel_shader=rim_palette, x=0,  y=0)
    menu.append(rim_sprite)

    #bg_bitmap = displayio.Bitmap(118, 150, 1)
    #bg_palette = displayio.Palette(1)
    #bg_palette[0] = 0x000000 #Black

    #bg_sprite = displayio.TileGrid(bg_bitmap, pixel_shader=bg_palette, x=5, y=5)
    #menu.append(bg_sprite)

    bh_colors = []
    bh_colors.append(0x004DFF)
    bh_colors.append(0x750787)
    bh_colors.append(0x008026)
    bh_colors.append(0xFFED00)
    bh_colors.append(0xFF8C00)
    bh_colors.append(0xE40303)

    # Draw a smaller colors
    for i in range(6):
        inner_bitmap = displayio.Bitmap(8, 8, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = bh_colors[i] # color
        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=120, y=100+(i*8))
        menu.append(inner_sprite)

    it = 0
    for opt in paths:
        it+=1
        
        menu_text0_group = displayio.Group(scale=1, x=8, y=10*it)
        #print(it)
        if currentselected == it:
            menu_text0_area = label.Label(terminalio.FONT, text=opt, color=0xFFFFFF)
        else:
            menu_text0_area = label.Label(terminalio.FONT, text=opt, color=0x777777)
        menu_text0_group.append(menu_text0_area)
        menu.append(menu_text0_group)

    display.show(menu)

# Make the display context
splash = displayio.Group()
display.show(splash)


color_bitmap = displayio.Bitmap(128, 160, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000  # black

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Create the slideshow object that plays through once alphabetically.
slideshow = SlideShow(display,
                      folder="/images",
                      loop=True,
                      order=PlayBackOrder.ALPHABETICAL,
                      dwell=2)
i=0

while slideshow.update():
    i+=1
    if i < 2:
        pass
    else:
        display.show(splash)
        time.sleep(1)
        break
    time.sleep(0.5)

selected = 1    
menu = displayio.Group()

dir_path = r'apps/'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if isfile(join(dir_path, path)):
        res.append(path)

DrawMenu(selected, res)

while True:
    if BTN_A.value == False:
        if selected == 1:
            pass
        else:
            selected-=1
            DrawMenu(selected, res)
            time.sleep(0.2)

    if BTN_B.value == False:
        if selected == len(res):
            pass
        else:
            selected+=1
            DrawMenu(selected, res)
        time.sleep(0.2)

    if BTN_X.value == False or BTN_Y.value == False:
        try:
            exec(open(join(dir_path, res[selected-1])).read())
        except:
            pass
        DrawMenu(selected, res)
    pass