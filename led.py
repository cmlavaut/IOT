import RPi.GPIO as gpio
import time

def main():
    gpio.setmode(gpio.BOARD)
    gpio.setup(8, gpio.out)

    while True:
        gpio.output(8,1)
        time.sleep(1)
        gpio.output(8,0)
        time.sleep(1)

if __name__ == "__main__":
    main()




