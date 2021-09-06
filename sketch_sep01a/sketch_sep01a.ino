#define ServoFeedback_R A9
#define ServoFeedback_L A8
#define Encoder_1 A6
#define Encoder_2 A5

void setup() {
  Serial.begin(19200);
  analogReadResolution(10);
}

void loop() {
  float volt_R = 0;
  float volt_L = 0;
  float encoderVal_1 = 0;
  float encoderVal_2 = 0;
  
  volt_R = analogRead(ServoFeedback_R) * 3.3/1024;
  volt_L = analogRead(ServoFeedback_L) * 3.3/1024;
  encoderVal_1 = analogRead(Encoder_1) * 3.3/1024;
  encoderVal_2 = analogRead(Encoder_2) * 3.3/1024;
  
  Serial.println(volt_R); 
  Serial.println(volt_L); 
  Serial.println(encoderVal_1); 
  Serial.println(encoderVal_2); 
  
  delay(100);
}
