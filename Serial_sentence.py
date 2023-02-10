import serial
#import RPi.GPIO as gpio
import time

def main():
    arduino = serial.Serial()
    try:
        puerto= input("poner com")
        arduino.port= 'COM' + puerto
        arduino.baudrate = 115200
        arduino.open()
    except  serial.serialutil.PortNotOpenError:
        print("no esta conectado a Windows")
        arduino.port == "/dev/ttyACM0"
        arduino.baudrate = 115200
        arduino.open()
    except:
        print("Arduino no conectado")


    while True:
        arduino.flushInput()
        msg = arduino.readline()
        msg = msg.decode()
        print(msg)
       
    

        
        time.sleep(1)
        
    arduino.close()


  

if __name__ == "__main__":

    main()
