# Paul Schakel
# reset_LEDs.py
# Resets a string of neopixel LEDs to their OFF state

import board
import neopixel

LED_COUNT = 150

def main():
    pixels = neopixel.NeoPixel(board.D18, LED_COUNT, brightness=0.2)
    pixels.fill((0, 0, 0))
    pixels.show()

if __name__ == "__main__":
    main()
