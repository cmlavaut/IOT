//ULTRASONIC

int pin =7;
int pin_IN=9;
unsigned long duration;
long distancia=0;
long dist1=0;
int temperatura;
int variable;
int lectura1 =0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(pin, OUTPUT);
pinMode(pin_IN, INPUT);
digitalWrite(pin, LOW);
pinMode(a5, INPUT); // entrada del sensor LM35
pinMode(a0, INPUT); // lectura de la fotoresistencia 

}

void loop() {
  // put your main code here, to run repeatedly:
sensortemp();
delay(200);
ultra1();
delay(200);
fotorresistencia();
delay(200);
Serial.println(String(temp_final)+","+String(distancia) + "," + String(lectura1));
}



void fotorresistencia(){
int lectura=analogRead(a0);
lectura1= map(lectura,0,1023,0,255);
}

void sensortemp (){
temperatura=analogRead(a5);
variable=map(temperatura, 0,1023,0,255);
float variable2 = variable*5;
float variable3 = variable2/255;
float temp_final= variable3 *100;
}



void ultra1(){
digitalWrite(pin, LOW);
delay(200);
digitalWrite(pin, HIGH);
delayMicroseconds(10);
digitalWrite(pin, LOW);
duration= pulseIn(pin_IN, HIGH); // duracion esta en micro segundos y mide cuando ve un flanco de subida
long distancia1= (duration*340);
long distancia2= distancia1/2;
distancia = distancia2/10000;
}
