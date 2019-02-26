# Grace
A library for easily coding advanced [NeoPixel](https://www.adafruit.com/category/168) light patterns with [CircuitPython](https://circuitpython.readthedocs.io). Grace takes its name from not only allowing beginners to "gracefully" code complex light sequences, but also from Grace Hopper, a pioneer of computer technology.

# Getting Started
Connect 3 NeoPixels to pin A0 of your CircuitPython-supported microcontroller. Connect the microcontroller to your computer and copy the contents of the `src` directory into the root of the CIRCUITPYTHON volume. The default program will immediately run causing the NeoPixels to light up in complex patterns.

The default program is written for [Adafruit Gemma M0](https://www.adafruit.com/product/3501) microcontrollers but will work with any CircuitPython-supported board.

# Customization
You can customize the light patterns by updating `code.py`.

You can customize the output pin and number of LEDs by updating `__init__.py` in the `grace` directory.
