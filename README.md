# BornHack 2022 Game On Badge

![BornHack 2022 Game On Badge](https://github.com/bornhack/badge2022/raw/hardware/IMAGES/badge-front.jpg "BornHack 2022 Game On Badge")

With this badge we are putting the focus on games. With the shape of a small controller and a color LCD screen in the middle it's ready for a bunch of interesting homebrew games.

This badge uses the RP2040 dualcore Cortex M0+ microcontroller from Raspberry Pi and has 16MB of Quad SPI flash for code and probably also a bit of media files.

The badge will come with [CircuitPython](https://circuitpython.org/) preloaded, for a very low barrier of entry, all you need is a USB-C cable, and your favourite texteditor and you are on your way to your own games.

In addition to screen and navigation buttons, there are are also a standard SAO v1.96bis connector and a Qwiic/Stemma QT connector for interfacing with modules in those eco-systems over I2C.

For those that want to experiment with expanding the badge with a bit more hardware, there is a prototyping area on the left side, maybe for a custom joystick, a preasure sensitive e-textile sensor or something else that works with your game. To interface with the RP2040, there are a few I/O hookup points along the exdge, that support either crocodile test leads, conductive thread or regular wire soldered down, depending on what you are making. Two of those I/O's have analog input capabilities, and there are two more analog inputs in the GPIO1 and GPIO2 pins of the SAO connector, if you need more.

There are also some mounting holes (they fit M3 screws), for mounting an additional add-on board or maybe a 3D printed case. If you want to make your own expansion board, there is [an add-on template](https://github.com/bornhack/badge2022/tree/add-on-template) (it's in the `add-on-template` branch in this repo), that you can open up and customize to your liking before ordering. There will also be some prototyping boards available in the Hardware Hacking Tent at BornHack along with some basic parts, similar to last year.

## CircuitPython restore file

If you flash the board with something else and want to get back to CircuitPython, you can bring the badge into the UF2 bootloader by holding the BOOT button and pressing RESET (you can also hold BOOT when powering on). The badge will then show up as a mass storage device called something like RP2-? which is the build in bootloader and you simply copy over the [firmware.uf2](https://github.com/bornhack/badge2022/raw/hardware/firmware.uf2) file from the root of this repository. The badge will reboot, and you are then back to CircuitPython

The original python files that was on the badge when handed out are in the [cp-init branch](https://github.com/bornhack/badge2022/tree/cp-init)

## Designed in KiCad v6

This board is designed in KiCad v6. To open the project, you will need to install a recent release version or one of the nightly builds, KiCad v5 won't open this design. The [schematic as a PDF](https://github.com/bornhack/badge2022/raw/hardware/schematic.pdf) is included for reference.

## Projects running on the badge

Feel free to submit a PR adding on to this list with your project that runs on the badge.

[Video player and AM radio transmitter](https://github.com/kbeckmann/bornhack-badge2022-audiovideo) by Konrad Beckmann. See it in action [here](https://twitter.com/kbeckmann/status/1556251282742075393) and [here](https://twitter.com/kbeckmann/status/1555895391463346176).


## License

The contents of this repository is released under the following license:

* the "Creative Commons Attribution-ShareAlike 4.0 International License"
  (CC BY-SA 4.0) full text of this license is included in the LICENSE file
  and a copy can also be found at
  [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)
