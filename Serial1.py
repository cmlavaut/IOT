import serial
#import RPi.GPIO as gpio
import time

def main():
    arduino = serial.Serial()
    try:
        arduino.port= 'COM3'
        arduino.baudrate = 9600
        arduino.open()
    except  serial.serialutil.PortNotOpenError:
        print("no esta conectado a Windows")
        arduino.port == "/dev/ttyACM0"
        arduino.baudrate = 9600
        arduino.open()
    except:
        print("Arduino no conectado")


    while True:
        arduino.flushInput()
        sensor = arduino.readline()
        sensor = sensor.decode()
        value= sensor.split(",")
        if (len(value)==3):
            print("temp:" , value[0])
            print("distancia:" , value[1])
            print("luz:" , value[2])
        else:
            print("valores incorrectos")
        
       
    

        
        time.sleep(1)
        
    arduino.close()


  

if __name__ == "__main__":

    main()
