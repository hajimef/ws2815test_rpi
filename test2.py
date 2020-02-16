import time
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 288       # number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 64  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

if __name__ == '__main__':
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    print("Press Ctrl-C to quit.")
    try:
        cp = 0
        while True:
            for i in range(0, 6):
                for j in range(0, LED_COUNT):
                    f = j % 6
                    c = ((j - f) / 6 + cp) % 3
                    if f == i:
                        if c == 0:
                            strip.setPixelColor(j, Color(255, 0, 0))
                        elif c == 1:
                            strip.setPixelColor(j, Color(0, 255, 0))
                        elif c == 2:
                            strip.setPixelColor(j, Color(0, 0, 255))
                    else:
                        strip.setPixelColor(j, Color(0, 0, 0))
                strip.show()
                time.sleep(0.1)
            cp -= 1
            cp %= 3

    except KeyboardInterrupt:
        for i in range(0, LED_COUNT):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
