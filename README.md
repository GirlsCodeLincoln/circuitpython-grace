# Grace
A library for easily coding advanced [NeoPixel](https://www.adafruit.com/category/168) light patterns with [CircuitPython](https://circuitpython.readthedocs.io). Grace takes its name from not only allowing beginners to "gracefully" code complex light sequences, but also from Grace Hopper, a pioneer of computer technology.

## Getting Started
Connect the microcontroller to your computer and copy the contents of the `src` directory into the root of the CIRCUITPYTHON volume. In `code.py`, update the `grace.configure()` command with your neopixel output pin and the number of neopixels you are using. The program will run as soon as you save the file on the CIRCUITPYTHON volume.

## Customization / Methods
You can customize the light patterns by updating `code.py`. The following methods are available:

### Speed / Timing
The following methods set the speed of the animations. The normal speed setting makes each simple command take 3 seconds.

- `grace.slowest()`
- `grace.slower()`
- `grace.slow()`
- `grace.normal()`
- `grace.fast()`
- `grace.faster()`
- `grace.fastest()`
- `grace.wait(0.5)` Waits for 1/2 second before the program continues

### Controls

- `grace.turn_on(1, color.red)` Turns on the first LED to red
- `grace.turn_off(2)` Turns off the second LED
- `grace.all_on(color.red)` Turns on all LEDs to red
- `grace.all_off()` Turns off all LEDs
- `grace.single(2, color.red)` Turns on the second LED to red and turns all other LEDs off
- `grace.pattern([color.red, color.green, color.blue])` Turns on the first LED to red, the second to green, and the third to blue

### Animations

- `grace.slide_out(color.red)` Animates a red pixel moving from the first LED to the last
- `grace.slide_in(color.red)` Animates a red pixel moving from the last LED to the first
- `grace.chase_out(color.red)` Animates a red pixel from the first LED to all LEDs
- `grace.chase_in(color.red)` Animates a red pixel from the last LED to all LEDs

### Complex Animations

- `grace.rainbow_cycle()` All pixels smothly change between colors
- `grace.rainbow_chase()` The rainbow moves through the LEDs
- `grace.rainbow_slide_out()` Does a slide_out for each color of the rainbow
- `grace.rainbow_slide_in()` Does a slide_in for each color of the rainbow

## Colors

There are two modules providing easy-to-use colors and sets of colors:

### `grace.color`

Provides a number of colors to use. Import it with `import grace.color as color`. The following colors are available:

- color.off
- color.red
- color.yellow
- color.green
- color.cyan
- color.blue
- color.purple
- color.white
- color.indigo
- color.orange

### `grace.colorset`

Provides `colorset.rainbow`, a list of all colors of the rainbow and `colorset.random(num)`, a method to provide a random list of colors from the rainbow. These are primariy for use within the grace animation library but they can also be used with `grace.pattern()`. Import it with `import grace.colorset as colorset`.
