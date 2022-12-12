
#include<Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;

String msg = "";

String str_angles[3];

int angle1 = 0;
int angle2 = 0;
int angle3 = 0;

int angle_prev1 = 0;
int angle_prev2 = 0;
int angle_prev3 = 0;

int count = 0;
int tmpi = 0;

void setup()
{
  Serial.begin(9600);
  
  servo1.attach(9);
  servo2.attach(10);
  servo3.attach(6);

  for(int i = 0; i < 3; i++)
  {
    str_angles[i] = ""; 
  }
  
  servo1.write(0);
    delay(100);
  servo2.write(0);
    delay(100);
  servo3.write(0);  
    delay(100);
}


void loop()
{
  if(Serial.available())
  {
    msg = Serial.readString();
    
    Serial.println("received: " + msg);

    count = 0;
    tmpi = 0;
    for(int i = 0; i < msg.length()-1; i++)
    {
      if(msg[i] == ' ')
      {
        if(count == 0)
        {
          str_angles[0] = msg.substring(0, i);
          tmpi = i;
        }
        else if(count == 1)
        {
          str_angles[1] = msg.substring(tmpi+1, i);
          tmpi = i;
          str_angles[2] = msg.substring(i+1, msg.length()-1);
          break;
        }
        count += 1;
      }
    }

    angle_prev1 = angle1;
    angle1 = str_angles[0].toInt();

    angle_prev2 = angle2;
    angle2 = str_angles[1].toInt();

    angle_prev3 = angle3;
    angle3 = str_angles[2].toInt();

        servo1.write( (int) (angle_prev1 + 0.4 * (angle1 - angle_prev1)) );
        delay(150);
        servo2.write( (int) (angle_prev2 + 0.4 * (angle2 - angle_prev2)) );
        delay(150);
        servo3.write( (int) (angle_prev3 + 0.4 * (angle3 - angle_prev3)) );
        delay(150);
        servo1.write( (int) (angle_prev1 + 0.7 * (angle1 - angle_prev1)) );
        delay(150);
        servo2.write( (int) (angle_prev2 + 0.7 * (angle2 - angle_prev2)) );
        delay(150);
        servo3.write( (int) (angle_prev3 + 0.7 * (angle3 - angle_prev3)) );
        delay(150);
        servo1.write( (int) (angle_prev1 + 1.0 * (angle1 - angle_prev1)) );
        delay(150);
        servo2.write( (int) (angle_prev2 + 1.0 * (angle2 - angle_prev2)) );
        delay(150);
        servo3.write( (int) (angle_prev3 + 1.0 * (angle3 - angle_prev3)) );
        delay(150);
        
    //Serial.println((String)angle1+ "|" + (String)angle2 + "|"+ (String)angle3);
  }
  else
  {
    delay(500);
  }
  delay(10);
}
