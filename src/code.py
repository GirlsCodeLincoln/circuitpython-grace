import grace
import grace.color as color
import grace.colorset as colorset

grace.init()

while True:
    grace.all_on(color.orange, 2)

    grace.pattern([color.red, color.green, color.blue], 2)

    grace.chase_out(color.red, 0.5)
    grace.chase_in(color.green, 0.5)

    grace.rainbow_cycle(0.01)

    grace.slide_out(color.purple, 0.1)
    grace.slide_in(color.purple, 0.1)
    grace.slide_out(color.purple, 0.1)
    grace.slide_in(color.purple, 0.1)
    grace.slide_out(color.purple, 0.1)
    grace.slide_in(color.purple, 0.1)

    grace.rainbow_chase(0.2)
    grace.rainbow_chase(0.2)
    grace.rainbow_chase(0.2)
    grace.rainbow_chase(0.2)
