#define ENCODER_OPTIMIZE_INTERRUPTS
#include <Encoder.h>

#define ServoFeedback_R A9
#define ServoFeedback_L A8
#define Encoder_1A 5 // A6
#define Encoder_1B 6 // A5
#define Encoder_2A 8 // A3
#define Encoder_2B 9 // A2

Encoder enc1(Encoder_1A, Encoder_1B);
Encoder enc2(Encoder_2A, Encoder_2B);

void setup() {
  Serial.begin(19200);
  delay(500);
  analogReadRes(10);
}

long pos1 = -999;
long pos2 = -999;

void loop() {
  long new1, new2; 
  new1 = enc1.read();
  new2 = enc2.read();

  if(new1 != pos1 || new2 != pos2) {
    pos1 = new1;
    pos2 = new2;
  }
  
  float volt_R = analogRead(ServoFeedback_R) * -180/561 + 260.8557;
  float volt_L = analogRead(ServoFeedback_L) * -180/585 + 259.0769 ;
  Serial.println(volt_R); 
  Serial.println(volt_L); 
  Serial.println(pos1);
  Serial.println(pos2); 
  
//  delay(100);
}
