# Grace
A library for easily coding advanced [NeoPixel](https://www.adafruit.com/category/168) light patterns with [CircuitPython](https://circuitpython.readthedocs.io). Grace takes its name from not only allowing beginners to "gracefully" code complex light sequences, but also from Grace Hopper, a pioneer of computer technology.

## Getting Started
Connect 3 NeoPixels to pin A0 of your CircuitPython-supported microcontroller. Connect the microcontroller to your computer and copy the contents of the `src` directory into the root of the CIRCUITPYTHON volume. The default program will immediately run causing the NeoPixels to light up in complex patterns.

The default program is written for [Adafruit Gemma M0](https://www.adafruit.com/product/3501) microcontrollers but will work with any CircuitPython-supported board.

## Customization
You can customize the light patterns by updating `code.py`.

You can customize the output pin and number of LEDs by updating `__init__.py` in the `grace` directory.

## Methods
The following methods are available:

`grace.turn_on(2, color.red, 0.5)` Turns on the second LED to red for 1/2 second

`grace.turn_off(2, 0.5)` Turns off the second LED

`grace.all_on(color.red, 0.5)` Turns on LEDs to red for 1/2 second

`grace.all_off(0.5)` Turns off all LEDs for 1/2 second

`grace.wait(0.5)` Waits for 1/2 second before the program continues

`grace.single(2, color.red, 0.5)` Turns on the second LED to red and turns all other LEDs off for 1/2 second

`grace.pattern([color.red, color.green, color.blue], 0.5)` Turns on the first LED to red, the second to green, and the third to blue for 1/2 second

`grace.slide_out(color.red, 0.1)` Animates a red pixel from the first LED to the last with a 0.1 second animation interval

`grace.slide_in(color.red, 0.1)` Animates a red pixel from the last LED to the first with a 0.1 second animation interval

`grace.chase_in(color.red, 0.1)` Animates a red pixel from the last LED to all LEDs with a 0.1 second animation interval

`grace.chase_out(color.red, 0.1)` Animates a red pixel from the first LED to all LEDs with a 0.1 second animation interval

`grace.rainbow_cycle(0.01)` A complex animation where all pixels gradually change between all colors with a 0.01 second animation interval

`grace.rainbow_chase(0.1)` A complex animation where the colors of the rainbow are moved through the LEDs

`grace.rainbow_slide_out(0.1)` Does a slide_out for each color of the rainbow

`grace.rainbow_slide_in(0.1)` Does a slide_in for each color of the rainbow

## Colors

There are two modules providing easy-to-use colors and sets of colors:

### grace.color

Provides a number of colors to use such as color.red and color.indigo.

### grace.colorset

Provides `colorset.rainbow`, a list of all colors of the rainbow and `colorset.random(num)`, a method to provide a random list of colors from the rainbow.
