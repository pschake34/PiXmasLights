# Paul Schakel
# fading_colors.py
# Fades between a certain number of colors randomly or in a set order

import time
import math
import random
import board
import neopixel

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = board.D18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_BRIGHTNESS = 0.3     # Set to 0 for darkest and 255 for brightest
MAX_BRIGHTNESS = 0.5
BLANK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (250, 57, 13)

pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write = False)
pixels.fill(BLANK)
pixels.show()

def fade_strip(speed):
    i = 0
    has_begun = False
    while True:
        pixels.brightness = (MAX_BRIGHTNESS / 2) * -1 * math.cos(0.15 * i) + (MAX_BRIGHTNESS / 2)
        pixels.show()
        i += 1
        time.sleep(speed)
        print(pixels.brightness)
        if pixels.brightness > 0 and not has_begun:
            has_begun = True
        elif round(pixels.brightness, 2) == 0 and has_begun:
            break

def main():
    random_order = True
    colors = [RED, GREEN, WHITE]
    speed = 0.25

    while True:
        if not random_order:
            for color in colors:
                pixels.fill(color)
                fade_strip(speed)
        else:
            pixels.fill(random.choice(colors))
            fade_strip(speed)


if __name__ == "__main__":
    main()
