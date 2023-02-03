import RPi.GPIO as gpio
import time

def main():
    gpio.setmode(gpio.BOARD)
    gpio.setup(8, gpio.OUT)
    gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_UP)
    
    while True:
        if gpio.input(10):
            gpio.output(8,1)
            time.sleep(0.1)
        else:
            gpio.output(8,0)
            time.sleep(0.1)

if __name__ == "__main__":
    main()




