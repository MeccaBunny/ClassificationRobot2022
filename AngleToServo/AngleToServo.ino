#include<Servo.h>


int servo1_pos, servo2_pos;



int RoPo1_Read; //Rotary Potentiometer
int RoPo2_Read;

Servo servo1;
Servo servo2;
//Servo servo3;

void setup() {
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  
  servo1.attach(9);
  servo2.attach(10);
  //servo3.attach(11);
}

void loop() {
  RoPo1_Read = analogRead(A0);
  RoPo2_Read = analogRead(A1);
  servo1_pos = map(RoPo1_Read,0,1023,0,180);
  servo2_pos = map(RoPo2_Read,0,1023,0,180);

  servo1.write(servo1_pos);
  servo2.write(servo2_pos);
  //servo3.write(servo3_pos);
}
