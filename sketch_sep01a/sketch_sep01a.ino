#define ServoFeedback_R A9

void setup() {
  Serial.begin(19200);
  analogReadResolution(10);
}

void loop() {
  float volt = 0;
  volt = analogRead(ServoFeedback_R) * 3.3/1024;
  Serial.println(volt); 
  delay(100);
}
