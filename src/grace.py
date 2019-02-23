import time
import random
import board
import neopixel
import color
import colorset

global pixels

def init():
    global pixels
    pixels = neopixel.NeoPixel(board.A0, 3, brightness=.2, auto_write=False)
    all_off()

def all_off(seconds = 0):
    all_on((0, 0, 0))
    pixels.show()
    wait(seconds)

def all_on(color, seconds = 0):
    for i in range(len(pixels)):
        pixels[i] = color
    pixels.show()
    wait(seconds)

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

def single(num, color, seconds = 0):
    pixel_set = [(0, 0, 0)] * len(pixels)
    pixel_set[num] = color
    pattern(pixel_set, seconds)

def pattern(colorList, seconds = 0):
    for i in range(len(colorList)):
        pixels[i] = colorList[i]
    pixels.show()
    wait(seconds)

def __slide(color, seconds, pixel_range):
    for num in pixel_range:
        single(num, color, seconds)
    all_off()

def slide_out(color, seconds = 0):
    __slide(color, seconds, range(len(pixels)))

def slide_in(color, seconds = 0):
    __slide(color, seconds, range(len(pixels) - 1, -1, -1))

def chase_out(color, seconds = 0.2):
    for i in range(len(pixels)):
        pixels[i] = color
        pixels.show()
        wait(seconds)

def chase_in(color, seconds = 0.2):
    for i in range(len(pixels) - 1, -1, -1):
        pixels[i] = color
        pixels.show()
        wait(seconds)

def rainbow_cycle(seconds = 0.01):
    for j in range(255):
        for i in range(len(pixels)):
            rc_index = (i * 256 // len(pixels)) + j
            pixels[i] = __wheel(rc_index & 255)
        pixels.show()
        wait(seconds)

def rainbow_chase(seconds = 0.1):
    for i in range(len(colorset.rainbow)):
        for j in range(len(pixels)):
            pixels[j] = colorset.rainbow[(i + j) % len(colorset.rainbow)]
        pixels.show()
        wait(seconds)

def rainbow_slide_out(seconds = 0.1):
    for i in range(len(colorset.rainbow)):
        slide_out(colorset.rainbow[i], seconds)

def rainbow_slide_in(seconds = 0.1):
    for i in range(len(colorset.rainbow)):
        slide_in(colorset.rainbow[i], seconds)

def turn_on(num, color, seconds = 0):
    pixels[num] = color
    pixels.show()
    wait(seconds)

def turn_off(num, seconds = 0):
    pixels[num] = (0, 0, 0)
    pixels.show()
    wait(seconds)

def wait(seconds):
    time.sleep(seconds)