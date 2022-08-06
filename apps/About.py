import board
import terminalio
import displayio
import digitalio
import pwmio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

about = displayio.Group()

about_group = displayio.Group(scale=1, x=8, y=30)
about_area = label.Label(terminalio.FONT, text="BornHack 2022", color=0xFFFFFF)
about_group.append(about_area)
about.append(about_group)

about_group = displayio.Group(scale=1, x=8, y=44)
about_area = label.Label(terminalio.FONT, text="Badge", color=0xFFFFFF)
about_group.append(about_area)
about.append(about_group)


about_group = displayio.Group(scale=1, x=8, y=70)
about_area = label.Label(terminalio.FONT, text="Details at:", color=0x777777)
about_group.append(about_area)
about.append(about_group)

about_group = displayio.Group(scale=1, x=8, y=84)
about_area = label.Label(terminalio.FONT, text="github.com/bornhack", color=0xFFFFFF)
about_group.append(about_area)
about.append(about_group)

about_group = displayio.Group(scale=1, x=8, y=98)
about_area = label.Label(terminalio.FONT, text="/badge2022", color=0xFFFFFF)
about_group.append(about_area)
about.append(about_group)


display.show(about)

time.sleep(10)
