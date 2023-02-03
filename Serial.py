import serial
import RPi.GPIO as gpio
import time

def main():
    arduino = serial.Serial()
    arduino.port = "/dev/ttyACM0"
    arduino.baudrate = 9600
    arduino.open()
    gpio.setmode(gpio.BOARD)
    gpio.setup(8,gpio.OUT)

    while True:
        sensor = arduino.readline()
        sensor = sensor.decode()
        
        try:
            value = float(sensor[6:11])
            if (value > 25.0):
                gpio.output(8,1)
            else:
                gpio.output(8,0)
            print(value)
        except:
            pass

    

        
        time.sleep(1)
        
    arduino.close()


  

if __name__ == "__main__":

    main()
