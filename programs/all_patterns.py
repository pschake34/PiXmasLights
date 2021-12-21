# Paul Schakel
# all_patterns.py
# Lets the user choose from all the different patterns I've created to run on my RGB Christmas tree

import time
import math
import threading
import random
import board
import neopixel

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = board.D18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_BRIGHTNESS = 0.3     # Set to 0 for darkest and 255 for brightest
BRIGHTNESS_DIFFERENCE = 0.1
BREATHING_SPEED_MAX = 0.4
BREATHING_SPEED_MIN = 0.01
BLANK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (250, 57, 13)

no_input = True

pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS)
pixels.fill(BLANK)
pixels.show()

# designed to be called as a thread
def signal_user_input():
    global no_input
    i = input("Hit enter to go back to menu")
    no_input = False
    # thread exits here


def basic_color():
    cycles = 0
    increase = False
    decrease = False
    previous_brightness = 0
    
    breathing_speed = (BREATHING_SPEED_MAX + BREATHING_SPEED_MIN) / 2   # set initial speed -- average of max and min

    while no_input:
        pixels.fill((250, 67, 5))
        pixels.show()

        if not increase and previous_brightness < pixels.brightness:    # checks if the first increasing section of curve has begun
            print("increase begins")
            increase = True
        elif increase and not decrease and previous_brightness > pixels.brightness:     # checks if decreasing section of curve has begun
            print("decrease begins")
            decrease = True
        elif increase and decrease and previous_brightness < pixels.brightness:     # checks if the curve has started next repetition, and changes the length of the curve if so
            breathing_speed = (random.random() * BREATHING_SPEED_MAX) + BREATHING_SPEED_MIN     # set new speed (length of curve)
            print("\nCycle ended - new speed is {}\n".format(breathing_speed))
            cycles = 0   # reset variables for next curve
            increase = False
            decrease = False

        previous_brightness = pixels.brightness
        pixels.brightness = (-1 * BRIGHTNESS_DIFFERENCE) * math.cos(breathing_speed * cycles) + LED_BRIGHTNESS  # changes brightness as "cycles" goes up - first value is always "LED_BRIGHTNESS"
        print(pixels.brightness)
        cycles += 1
        time.sleep(0.1)


def chasing_lights(num_groups):
    groups = [[0, 1, 2, 3, 4] for group in range(num_groups)]
    active_groups = [False for group in groups]
    active_groups[0] = True
    colors = [RED, GREEN, WHITE]
    group_colors = [i % len(colors) for i in range(num_groups)]

    delay = int((LED_COUNT) / num_groups)
    print(delay)

    while no_input:
        for i in range(num_groups):
            group = groups[i]
            if active_groups[i]:
                pixels[group[0]] = BLANK

                for j in range(len(group)):
                    if group[j] == LED_COUNT-1:
                        group[j] = 0
                    else:
                        group[j] += 1
                    pixels[group[j]] = colors[group_colors[i]]
            elif not active_groups[i] and groups[i-1][0] == delay:
                active_groups[i] = True

        pixels.show()
        time.sleep(0.01)
        print(groups)


def main():
    global no_input
    
    while True:
        print("\n\nProgram options: ")
        print("0. Clear Lights\n1. Basic Color\n2. Chasing Lights")
        choice = int(input("Enter selection: "))

        if choice == 0:
            pixels.fill(BLANK)
            pixels.show()

        elif choice == 1:
            # we're just going to wait for user input while other functions do stuff...
            t = threading.Thread(target = signal_user_input)
            t.start()
            basic_color()
            no_input = True

        elif choice == 2:
            num_groups = int(input("Enter the number of groups: "))

            # we're just going to wait for user input while other functions do stuff...
            t = threading.Thread(target = signal_user_input)
            t.start()
            chasing_lights(num_groups)
            no_input = True


if __name__ == "__main__":
    main()
