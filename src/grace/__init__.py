import time
import neopixel
import grace.colorset as colorset

global pixels
__interval = 3

def configure(pin, num_pixels, brightness):
    global pixels
    pixels = neopixel.NeoPixel(pin, num_pixels, brightness=brightness, auto_write=False)
    all_off()

def set_brightness(brightness):
    global pixels
    pixels.brightness = brightness

def dont_wait():
    global __interval
    __interval = 0

def fastest():
    global __interval
    __interval = 0.3

def faster():
    global __interval
    __interval = 0.7

def fast():
    global __interval
    __interval = 1.2

def normal():
    global __interval
    __interval = 3

def slow():
    global __interval
    __interval = 5

def slower():
    global __interval
    __interval = 8

def slowest():
    global __interval
    __interval = 12

def all_off():
    all_on((0, 0, 0))

def all_on(color):
    pixels.fill(color)
    pixels.show()
    wait(__interval)

def __wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def __single_no_wait(num, color):
    pixel_set = [(0, 0, 0)] * len(pixels)
    pixel_set[num] = color
    __pattern_no_wait(pixel_set)

def single(num, color):
    __single_no_wait(num - 1, color)
    wait(__interval)

def __pattern_no_wait(colorList):
    for i in range(min(len(colorList), len(pixels))):
        pixels[i] = colorList[i]
    pixels.show()

def pattern(colorList):
    __pattern_no_wait(colorList)
    wait(__interval)

def __slide(color, pixel_range):
    for num in pixel_range:
        __single_no_wait(num, color)
        wait(__interval / 3)

def slide_out(color):
    __slide(color, range(len(pixels)))

def slide_in(color):
    __slide(color, range(len(pixels) - 1, -1, -1))

def chase_out(color):
    for i in range(len(pixels)):
        pixels[i] = color
        pixels.show()
        wait(__interval / 3)

def chase_in(color):
    for i in range(len(pixels) - 1, -1, -1):
        pixels[i] = color
        pixels.show()
        wait(__interval / 3)

def rainbow_cycle():
    for j in range(255):
        for i in range(len(pixels)):
            rc_index = (i * 256 // len(pixels)) + j
            pixels[i] = __wheel(rc_index & 255)
        pixels.show()
        wait(__interval / 100)

def rainbow_chase():
    for i in range(len(colorset.rainbow) * 2):
        for j in range(len(pixels)):
            pixels[j] = colorset.rainbow[(i + j) % len(colorset.rainbow)]
        wait(__interval / 6)
        pixels.show()

def rainbow_slide_out():
    for i in range(len(colorset.rainbow)):
        slide_out(colorset.rainbow[i])

def rainbow_slide_in():
    for i in range(len(colorset.rainbow)):
        slide_in(colorset.rainbow[i])

def turn_on(num, color):
    pixels[num - 1] = color
    pixels.show()
    wait(__interval)

def turn_off(num):
    pixels[num - 1] = (0, 0, 0)
    pixels.show()
    wait(__interval)

def wait(seconds):
    time.sleep(seconds)