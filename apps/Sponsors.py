import displayio

from adafruit_slideshow import PlayBackOrder, SlideShow

splash = displayio.Group()
display.show(splash)

# Create the slideshow object that plays through once alphabetically.
sponsors = SlideShow(display,
                      folder="/sponsors",
                      loop=False,
                      order=PlayBackOrder.ALPHABETICAL,
                      dwell=1)

while sponsors.update():
    pass
