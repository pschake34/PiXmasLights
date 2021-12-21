# Paul Schakel
# random_fade.py
# Simple breathing lights that mimic the color of a basic incandescent bulb while their brightness changes with an overengineered cosine function

import time
import math
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

def main():
    pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS)
    pixels.fill((0, 0, 0))
    pixels.show()

    cycles = 0
    increase = False
    decrease = False
    previous_brightness = 0
    
    breathing_speed = (BREATHING_SPEED_MAX + BREATHING_SPEED_MIN) / 2
    while True:
        pixels.fill((250, 67, 5))
        pixels.show()

        if not increase and previous_brightness < pixels.brightness:    #checks if the first increasing section of curve has begun
            print("increase begins")
            increase = True
        elif increase and not decrease and previous_brightness > pixels.brightness:     #checks if decreasing section of curve has begun
            print("decrease begins")
            decrease = True
        elif increase and decrease and previous_brightness < pixels.brightness:     #checks if the curve has started next repetition, and changes the length of the curve if so
            breathing_speed = (random.random() * BREATHING_SPEED_MAX) + BREATHING_SPEED_MIN     #set new speed (length of curve)
            print("\nCycle ended - new speed is {}\n".format(breathing_speed))
            cycles = 0   #reset variables for next curve
            increase = False
            decrease = False

        previous_brightness = pixels.brightness
        pixels.brightness = (-1 * BRIGHTNESS_DIFFERENCE) * math.cos(breathing_speed * cycles) + LED_BRIGHTNESS  #changes brightness as "cycles" goes up - first value is always "LED_BRIGHTNESS"
        print(pixels.brightness)
        cycles += 1
        time.sleep(0.1)

if __name__ == "__main__":
    main()
