# Paul Schakel
# alternating_colors.py
# Flashes between two different colors

import time
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


def main():
    pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write = False)
    pixels.fill(BLANK)
    pixels.show()

    color1 = RED
    color2 = WHITE
    speed = 0.75

    for i in range(LED_COUNT):
        if i % 2  == 0:
            pixels[i] = color1
        else:
            pixels[i] = color2
        pixels.show()
        time.sleep(0.1)


    while True:
        for i in range(LED_COUNT):
            if pixels[i] == list(color1):
                pixels[i] = color2
            elif pixels[i] == list(color2):
                pixels[i] = color1
        
        for i in range(LED_COUNT-1, -1, -1):
            pixels.show()
            time.sleep(0.001)

        time.sleep(speed)
        print(pixels)

if __name__ == "__main__":
    main()
