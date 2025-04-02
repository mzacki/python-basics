import random
import sys
import time

W, H = 80, 30  # width and height of the screen
DECAY = 28  # speed of a char fade out (going from white to black)

buf = bytearray(W * H)  # graphical buffer of frames
droplets = []


def iterate():  # decreases opacity of chars - fade out effect
    global droplets

    for y in range(H):  # for each char in a line
        for x in range(W):
            v = buf[x + y * W]  # calculate char fade out value (design pattern)
            v -= DECAY
            if v < 0:
                v = 0
            buf[x + y * W] = v

    while len(droplets) < int(W * 1.5):  # how many droplets in a screen (rounded to integer)
        # create new droplet if there are less than limit
        droplet = [random.randint(0, W - 1),  # calculates horizontal position of a new char
                   0,  # starts from vertical 0 position
                   1 + random.random() * 1.5  # speed of a droplet
                   ]
        droplets.append(droplet)

    new_droplets = []
    for droplet in droplets:

        x, y, speed = droplet  # idiom: desctructuring of an object
        next_y = y + speed  # physics: new position is old position plus quantum of time :)

        skip_droplet = False
        for i in range(int(y), int(next_y) + 1):  # add white colour to fast moving droplet
            if i >= H:  # if a droplet goes outside the screen...
                skip_droplet = True  # do not process such droplet anymore
                break
            buf[x + i * W] = 255

        if not skip_droplet:
            droplet[1] = next_y  # update position of a droplet
            new_droplets.append(droplet)

    droplets = new_droplets


CHARSET = [chr(x) for x in range(0x30a1, 0x30fb)]


def draw():
    o = ["\x1b[2J\x1b[1;1H"]

    for y in range(H):
        for x in range(W):
            v = buf[x + y * W]

            if v >= 128:
                r = (v - 128) * 2
                g = 255
                b = (v - 128) * 2
            else:
                r = 0
                g = v * 2
                b = 0

            ch = CHARSET[(x * 15263 + y * 91263) % len(CHARSET)]
            o.append(f"\x1b[38;2;{r};{g};{b}m{ch}\x1b[m")
        o.append("\n")

    sys.stdout.write(''.join(o))
    sys.stdout.flush()


while True:
    iterate()
    draw()
    time.sleep(0.1)
