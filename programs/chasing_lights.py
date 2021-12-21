# Paul Schakel
# chasing_lights.py
# Makes small groups of lights appear to chase each other up the tree

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

num_groups = 6

def main():
    pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS)
    pixels.fill(BLANK)
    pixels.show()

    
    groups = [[0, 1, 2, 3, 4] for group in range(num_groups)]
    active_groups = [False for group in groups]
    active_groups[0] = True
    colors = [RED, GREEN, WHITE]
    group_colors = [i % len(colors) for i in range(num_groups)]

    delay = int((LED_COUNT) / num_groups)
    print(delay)

    while True:
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

if __name__ == "__main__":
    main()
