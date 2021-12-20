# Paul Schakel
# test_LEDS.py
# Initial test for RGB light strings connected to a raspberry pi

import board
import neopixel
import time

# LED strip configuration:
LED_COUNT      = 50      # Number of LED pixels.
LED_PIN        = board.D18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_BRIGHTNESS = 0.3     # Set to 0 for darkest and 255 for brightest

def main():
    pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=LED_BRIGHTNESS)
    pixels.fill((0, 0, 0))
    time.sleep(2)
    print("LEDs initialized")

    j = 1
    while True:
        j += 1
        for i in range(LED_COUNT):
            pixels[i] = (255, 0, 0)
            pixels.show()
            time.sleep(0.01)

        for i in range(LED_COUNT):
            pixels[i] = (0, 0, 0)
            pixels.show()
            time.sleep(0.01)
        
        #pixels.fill((255, 0, 0))
        #pixels.show()
        #print("set to red")
        #time.sleep(2)

        #pixels.fill((0, 255, 0))
        #pixels.show()
        #print("set to green")	
        #time.sleep(2)

        print("repetition {}".format(j))

if __name__ == "__main__":
    main()
