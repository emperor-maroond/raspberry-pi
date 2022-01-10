#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>
#include <ResponsiveAnalogRead.h>

#define ServoFeedback_R A9
#define ServoFeedback_L A8
#define Encoder_1A 5 // A6
#define Encoder_1B 6 // A5
#define Encoder_2A 8 // A3
#define Encoder_2B 9 // A2
#define Encoder_3A 19
#define Encoder_3B 18
#define LED 13

#define V_Line 11
#define Reset_Enc 12

ResponsiveAnalogRead anaR(ServoFeedback_R, true);
ResponsiveAnalogRead anaL(ServoFeedback_L, true);
Encoder enc1(Encoder_1A, Encoder_1B);
Encoder enc2(Encoder_2A, Encoder_2B);
Encoder enc3(Encoder_3A, Encoder_3B);

void setup() {
  Serial.begin(9600);
  delay(500);
  analogReadRes(10);
  pinMode(LED, OUTPUT);
  pinMode(V_Line, OUTPUT);
  pinMode(Reset_Enc, INPUT);
  digitalWrite(LED, HIGH);
  digitalWrite(V_Line, HIGH);
}

long pos1 = -999;
long pos2 = -999;
long pos3 = -999;
elapsedMillis i = 0;

float volt_R = 0;
float volt_L = 0;
float tmp1 = 0;
float tmp2 = 0;
float tmp3 = 0;
float divider = 0;
bool h = 1; 

void loop() {
  anaR.update();
  anaL.update();
  long new1, new2, new3; 
  new1 = enc1.read();
  new2 = enc2.read();
  new3 = enc3.read();

  if(new1 != pos1 || new2 != pos2 || new3 != pos3) {
    pos1 = new1;
    pos2 = new2;
    pos3 = new3;
  }
  
  if(digitalRead(Reset_Enc) == HIGH){
    enc1.write(0);
    enc2.write(0);
    enc3.write(0);
  }
  
  volt_R = volt_R + anaR.getValue() * -180/561.0 + 260.8557;
  volt_L = volt_L + anaL.getValue() * -180/585.0 + 259.0769;
  tmp1 = tmp1 + pos1;
  tmp2 = tmp2 + pos2;
  tmp3 = tmp3 + pos3;
  divider ++;
  
  if(i >= 10){
    Serial.print("a");
    Serial.println(180 - volt_R/divider); 
    Serial.print("b");
    Serial.println(volt_L/divider); 
    Serial.print("c");  
//    Serial.println(//pos1);
    Serial.println(tmp1/divider*767.0/8585.0+13.2);
    Serial.print("d");  
    Serial.println(tmp2/divider*360.0/(-1440.333)*M_PI/180*0.02); 
    Serial.print("e"); 
    Serial.println(tmp3/divider*(-8)/53+90); 
    i = 0;
    volt_R = 0;
    volt_L = 0;
    tmp1 = 0;
    tmp2 = 0;
    tmp3 = 0;
    divider = 0;
    if(h==1){
      digitalWrite(LED, LOW);
      h = 0;
    }
    else{
      digitalWrite(LED, HIGH);
      h = 1;
    }
    
  }
//  delay(100);
}
