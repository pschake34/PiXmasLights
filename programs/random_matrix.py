# Paul Schakel
# random_matrix.py
# Makes the LEDs turn on and off randomly kind of like a random matrix

import time
import random
import board
import neopixel

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = board.D18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_BRIGHTNESS = 0.3     # Set to 0 for darkest and 255 for brightest
BLANK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (250, 57, 13)

color = WHITE

def main():
    pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS)
    pixels.fill(BLANK)
    pixels.show()

    for i in range(len(pixels)):
        pixels[i] = color
        pixels.show()
        time.sleep(0.05)

    time.sleep(1)

    while True:
        i = random.randint(0, LED_COUNT-1)
        state = random.choice([0, 1])

        if state:
            pixels[i] = color
        else:
            pixels[i] = BLANK
        pixels.show()
        time.sleep(0.005)

if __name__ == "__main__":
    main()

