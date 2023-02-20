import serial
#import RPi.GPIO as gpio
import time
import sys

def main():
    arduino = serial.Serial()
    arduino2= serial.Serial()
    try:
        puerto1= sys.argv[1]
        puerto2= sys.argv[2]
        arduino.port= 'COM' + puerto1
        arduino2.port = 'COM' + puerto2
        arduino.baudrate = 115200
        arduino2.baudrate = 115200
        arduino.open()
        arduino2.open()
    except:
        try:
            arduino.port = "/dev/ttyACM0"
            arduino.baudrate = 9600
            print(arduino.port)
            arduino.open()
        except:
            print("nothing conected")
            quit()

     
    while True:
        arduino.flushInput()
        sensor = arduino.readline()
        sensor = sensor.decode()
        value= sensor.split()
        arduino2.flushInput()
        sensor11 = arduino2.readline()
        sensor11 = sensor11.decode()
        value11 = sensor11.split()
        if (len(value)==5 and len(value11)==5):
            print(" ".join(value[:2]))
            print("humedad suelo: " , value[2])
            print("humedad relativa: " , value[3])
            print("temperatura: " , value[4])
            print(" ".join(value11[:2]))
            print("humedad suelo: ", value11[2])
            print("humedad relativa: ", value11[3])
            print("temperatura: ", value11[4])
        else:
            print("valores incorrectos")
    
       
            
        time.sleep(3)
        
    arduino.close()


  

if __name__ == "__main__":

    main()
