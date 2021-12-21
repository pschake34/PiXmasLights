# Paul Schakel
# find_rgb_values.py
# Makes finding exact colors more simple

import board
import neopixel

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = board.D18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_BRIGHTNESS = 0.3     # Set to 0 for darkest and 255 for brightest

def main():
    r = 0
    g = 0
    b = 0

    pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS)
    pixels.fill((0, 0, 0))
    pixels.show()
    
    while True:
        pixels.fill((r, g, b))
        pixels.show()

        print("RGB Values:")
        r = int(input("Red value (currently {}): ".format(r)))
        g = int(input("Green value (currently {}): ".format(g)))
        b = int(input("Blue value (currently {}): ".format(b)))

if __name__ == "__main__":
    main()
   