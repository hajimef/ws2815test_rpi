import time
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 288       # number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 64  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

colors = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 1]
]

if __name__ == '__main__':
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    print("Press Ctrl-C to quit.")
    try:
        while True:
            for i in range(0, len(colors)):
                for j in range(0, 510, 5):
                    c = 255 - abs(j - 255)
                    for k in range(0, LED_COUNT):
                        r = c if colors[i][0] else 0
                        g = c if colors[i][1] else 0
                        b = c if colors[i][2] else 0
                        strip.setPixelColor(k, Color(r, g, b))
                    strip.show()
                    time.sleep(0.01)

    except KeyboardInterrupt:
        for i in range(0, LED_COUNT):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
