import serial
#import RPi.GPIO as gpio
import time
import sys

def main():
    arduino = serial.Serial()
    try:
        puerto= sys.argv[1]
        arduino.port= 'COM' + puerto
        arduino.baudrate = 115200
        arduino.open()
    except:
        try:
            arduino.port = "/dev/ttyACM0"
            arduino.baudrate = 9600
            print(arduino.port)
            arduino.open()
        except:
            print("Arduino no conectado")
            quit()

     
    while True:
        arduino.flushInput()
        sensor = arduino.readline()
        sensor = sensor.decode()
        value= sensor.split(",")
        if (len(value)==4):
            print("temp:" , value[0])
            print("distancia:" , value[1])
            print("luz:" , value[2])
            print("temp1:" , value[3])
        
        else:
            print("valores incorrectos")
        
       
    

        
        time.sleep(1)
        
    arduino.close()


  

if __name__ == "__main__":

    main()
