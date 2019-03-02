import board
import grace
import grace.color as color

grace.configure(pin = board.A0, num_pixels = 3, brightness = 0.2)

while True:
    grace.normal()

    grace.rainbow_slide_in()

    grace.rainbow_cycle()

    grace.all_on(color.orange)
    grace.all_off()

    grace.pattern([color.red, color.white, color.blue])

    grace.chase_out(color.yellow)
    grace.chase_in(color.green)

    grace.slide_out(color.blue)
    grace.slide_in(color.yellow)

    grace.rainbow_cycle()

    grace.fast()
    grace.slide_out(color.purple)
    grace.slide_in(color.purple)
    grace.normal()

    grace.rainbow_chase()