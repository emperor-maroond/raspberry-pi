#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>
#include <math.h>

#define ServoFeedback_R A9
#define ServoFeedback_L A8
#define Encoder_1A 5 // A6
#define Encoder_1B 6 // A5
#define Encoder_2A 8 // A3
#define Encoder_2B 9 // A2

#define V_Line 0
#define Reset_Enc 12

Encoder enc1(Encoder_1A, Encoder_1B);
Encoder enc2(Encoder_2A, Encoder_2B);

void setup() {
  Serial.begin(9600);
  delay(500);
  analogReadRes(10);
  pinMode(V_Line, OUTPUT);
  pinMode(Reset_Enc, INPUT);
  digitalWrite(V_Line, LOW);
}

long pos1 = -999;
long pos2 = -999;
elapsedMillis i = 0;

float volt_R = 0;
float volt_L = 0;
float tmp1 = 0;
float tmp2 = 0;
float divider = 0;

void loop() {
  long new1, new2; 
  new1 = enc1.read();
  new2 = enc2.read();

  if(new1 != pos1 || new2 != pos2) {
    pos1 = new1;
    pos2 = new2;
  }
  
  if(digitalRead(Reset_Enc) == LOW){
    enc1.write(0);
    enc2.write(0);
  }
  
  volt_R = volt_R + analogRead(ServoFeedback_R) * -180/561.0 + 260.8557;
  volt_L = volt_L + analogRead(ServoFeedback_L) * -180/585.0 + 259.0769;
  tmp1 = tmp1 + pos1;
  tmp2 = tmp2 + pos2;
  divider ++;
  
  if(i >= 0){
//    Serial.print("a");
//    Serial.println(volt_R/divider); 
//    Serial.print("b");
//    Serial.println(volt_L/divider); 
//    Serial.print("c");  
    Serial.println(pos1);
//    Serial.println(tmp1/divider*4207.0/45505.0+5.76);
//    Serial.print("d");  
//    Serial.println(tmp2/divider*360.0/(-1440.333)*M_PI/180*0.02); 
//    i = 0;
//    volt_R = 0;
//    volt_L = 0;
//    tmp1 = 0;
//    tmp2 = 0;
//    divider = 0;
  }
//  delay(100);
}
