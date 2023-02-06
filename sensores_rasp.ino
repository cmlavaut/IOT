//ULTRASONIC

int pin =7;
int pin_IN=9;
unsigned long duration;
long distancia=0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(pin, OUTPUT);
pinMode(pin_IN, INPUT);
digitalWrite(pin, LOW);


}

void loop() {
  // put your main code here, to run repeatedly:
long distancia = ultra1();
int lectura = fotorresistencia();
float temp_final= sensortemp();
delay(200);
Serial.println(String(temp_final)+","+String(distancia) + "," + String(lectura));
}


int fotorresistencia(){
int lectura=analogRead(A0);
return map(lectura,0,1023,0,255);
}

float sensortemp (){
float temperatura=analogRead(A4);
float variable=map(temperatura, 0,1023,0,255);
return variable*500/255;
}


long ultra1(){
digitalWrite(pin, LOW);
delay(200);
digitalWrite(pin, HIGH);
delayMicroseconds(10);
digitalWrite(pin, LOW);
duration= pulseIn(pin_IN, HIGH); // duracion esta en micro segundos y mide cuando ve un flanco de subida
distancia= (duration*340);
distancia= distancia/2;
return distancia/10000;
}
