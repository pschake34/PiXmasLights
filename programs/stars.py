# Paul Schakel
# stars.py
# Makes a set number of stars fade in and then out

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


def fade(color, amount):
    return tuple([int(value*amount) for value in color])


def main():
    pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS)
    pixels.fill(BLANK)
    pixels.show()

    num_stars = LED_COUNT / 2
    stars = {}
    star_stages = {}
    to_remove = []
    color = WHITE
    speed = 0.01

    while True:
        if len(stars) < num_stars and round(random.random()*3) == 2:
            while True: # makes sure duplicates cant occur
                new_index = random.randint(0, LED_COUNT-1)
                if new_index in stars:
                    print("duplicate")
                    continue
                else:
                    stars[new_index] = 0.1
                    star_stages[new_index] = False
                    break

        for index, brightness in stars.items():
            pixels[index] = fade(color, brightness)
            if star_stages[index]:
                stars[index] -= 0.1
            else:
                stars[index] += 0.1
            
            if round(stars[index], 3) == 0: # had to round because the floats deviate from integers to a certain degree
                pixels[index] = BLANK
                to_remove.append(index)
            elif round(stars[index], 3) == 1:
                star_stages[index] = True

            time.sleep(speed)
            pixels.show()
        
        for index in to_remove: # takes the item removal out of the main for loop because otherwise the main for loop wont work
            stars.pop(index)
            star_stages.pop(index)

        to_remove = []


if __name__ == "__main__":
    main()
