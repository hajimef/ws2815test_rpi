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
    Color(255, 0, 0), Color(255, 32, 0), Color(255, 64, 0),Color(255, 96, 0), Color(255, 128, 0), Color(255, 160, 0), Color(255, 192, 0), Color(255, 224, 0),
    Color(255, 255, 0), Color(224, 255, 0), Color(192, 255, 0), Color(160, 255, 0), Color(128, 255, 0), Color(96, 255, 0), Color(64, 255, 0), Color(32, 255, 0),
    Color(0, 255, 0), Color(0, 255, 32), Color(0, 255, 64), Color(0, 255, 96), Color(0, 255, 128), Color(0, 255, 160), Color(0, 255, 192), Color(0, 255, 224),
    Color(0, 255, 255), Color(0, 224, 255), Color(0, 192, 255), Color(0, 160, 255), Color(0, 128, 255), Color(0, 96, 255), Color(0, 64, 255), Color(0, 32, 255),
    Color(0, 0, 255), Color(32, 0, 255), Color(64, 0, 255), Color(96, 0, 255), Color(128, 0, 255), Color(160, 0, 255), Color(192, 0, 255), Color(224, 0, 255),
    Color(255, 0, 255), Color(255, 0, 224), Color(255, 0, 192), Color(255, 0, 160), Color(255, 0, 128), Color(255, 0, 96), Color(255, 0, 64), Color(255, 0, 32)
]
ptr = 0

if __name__ == '__main__':
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    print("Press Ctrl-C to quit.")
    try:
        while True:
            for i in range(0, LED_COUNT):
                p = (i + ptr) % len(colors)
                strip.setPixelColor(i, colors[p])
            strip.show()
            ptr += 1
            ptr %= len(colors)
            time.sleep(0.05)

    except KeyboardInterrupt:
        for i in range(0, LED_COUNT):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
