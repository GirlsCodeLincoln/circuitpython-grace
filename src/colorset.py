import color

rainbow = [color.red, color.orange, color.yellow, color.green, color.blue, color.indigo]

def random(num):
    randomList = random.shuffle(rainbow)
    for i in range(num):
        yield rainbow[i % len(rainbow)]
