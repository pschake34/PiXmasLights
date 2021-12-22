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
MAX_BRIGHTNESS = 0.5
BRIGHTNESS_DIFFERENCE = 0.1
BREATHING_SPEED_MAX = 0.4
BREATHING_SPEED_MIN = 0.01
BLANK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (250, 57, 13)
BLUE = (0, 0, 255)
ORANGE = (250, 40, 0)
YELLOW = (255, 128, 0)
PURPLE = (150, 0, 250)
PINK = (250, 0, 150)

no_input = True

pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write = False)
pixels.fill(BLANK)
pixels.show()

# designed to be called as a thread
def signal_user_input():
    global no_input
    i = input("Hit enter to go back to menu")
    no_input = False
    # thread exits here


def fade(color, amount):
    return tuple([int(value*amount) for value in color])


def fade_strip(speed):
    x = 0
    has_begun = False
    while no_input:
        pixels.brightness = (MAX_BRIGHTNESS / 2) * -1 * math.cos(0.15 * x) + (MAX_BRIGHTNESS / 2)
        pixels.show()
        x += 1
        time.sleep(speed)
        print(pixels.brightness)
        if pixels.brightness > 0 and not has_begun:
            has_begun = True
        elif round(pixels.brightness, 2) == 0 and has_begun:
            break


def get_color():
    color_choice = int(input("\n1. Red\n2. Green\n3. White\n4. Blue\n5. Orange\n6. Yellow\n7. Purple\n8. Pink\n9. Define your own\nEnter selection: "))
    colors = [RED, GREEN, WHITE, BLUE, ORANGE, YELLOW, PURPLE, PINK]

    if color_choice == 4:
        r = int(input("R: "))
        g = int(input("G: "))
        b = int(input("B: "))
        return (r, g, b)
    else:
        return colors[color_choice-1]


def get_speed(default):
    speed = input("Enter speed (Return for default of {}): ".format(default))
    if speed == "":
        return default
    return float(speed)


def basic_color(color):
    cycles = 0
    increase = False
    decrease = False
    previous_brightness = 0
    
    breathing_speed = (BREATHING_SPEED_MAX + BREATHING_SPEED_MIN) / 2   # set initial speed -- average of max and min

    while no_input:
        pixels.fill(color)
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


def chasing_lights(num_groups, speed):
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
        time.sleep(speed)


def random_matrix(color):
    pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS)
    pixels.fill(BLANK)
    pixels.show()

    for i in range(len(pixels)):
        pixels[i] = color
        pixels.show()
        time.sleep(0.05)

    time.sleep(1)

    while no_input:
        i = random.randint(0, LED_COUNT-1)
        state = random.choice([0, 1])

        if state:
            pixels[i] = color
        else:
            pixels[i] = BLANK
        pixels.show()
        time.sleep(0.005)


def stars(color, speed):
    num_stars = LED_COUNT / 2
    stars = {}
    star_stages = {}
    to_remove = []

    while no_input:
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


def alternating_colors(color1, color2, speed):
    for i in range(LED_COUNT):
        if i % 2  == 0:
            pixels[i] = color1
        else:
            pixels[i] = color2
        pixels.show()
        time.sleep(0.1)

    while no_input:
        for i in range(LED_COUNT):
            if pixels[i] == list(color1):
                pixels[i] = color2
            elif pixels[i] == list(color2):
                pixels[i] = color1
        
        for i in range(LED_COUNT-1, -1, -1):
            pixels.show()
            time.sleep(0.001)

        time.sleep(speed)


def fading_colors(colors, speed, random_order):
    while no_input:
        if not random_order:
            for color in colors:
                pixels.fill(color)
                fade_strip(speed)
        else:
            pixels.fill(random.choice(colors))
            fade_strip(speed)


def main():
    global no_input
    
    while True:
        pixels.fill(BLANK)
        pixels.show()

        print("\n\nProgram options: ")
        print("0. Exit\n1. Basic Color\n2. Chasing Lights\n3. Random Matrix\n4. Stars\n5. Alternating Colors\n6. Fading Colors")
        choice = int(input("Enter selection: "))

        if choice == 0:
            break

        # we're just going to wait for user input while other functions do stuff...
        t = threading.Thread(target = signal_user_input)

        if choice == 1:
            color = get_color()
            t.start() # have to wait until after user input
            basic_color(color)

        elif choice == 2:
            num_groups = int(input("Enter the number of groups: "))
            speed = get_speed(0.1)
            t.start() # have to wait until after user input
            chasing_lights(num_groups, speed)

        elif choice == 3:
            color = get_color()
            t.start()
            random_matrix(color)

        elif choice == 4:
            color = get_color()
            speed = get_speed(0.01)
            t.start()
            stars(color, speed)

        elif choice == 5:
            color1 = get_color()
            color2 = get_color()
            speed = get_speed(0.75)
            t.start()
            alternating_colors(color1, color2, speed)

        elif choice == 6:
            colors = []
            num_colors = int(input("Enter the number of colors: "))
            i = 0
            while i < num_colors:
                colors.append(get_color())
                i += 1

            speed = get_speed(0.25)
            random_choice = input("Random? Y/n: ").lower()
            is_random = False
            if random_choice == "" or random_choice == "y":
                is_random = True

            t.start()
            fading_colors(colors, speed, is_random)
            
        no_input = True


if __name__ == "__main__":
    main()
