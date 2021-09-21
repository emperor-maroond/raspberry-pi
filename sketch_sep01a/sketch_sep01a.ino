#define ServoFeedback_R A9
#define ServoFeedback_L A8
#define Encoder_1A 20 // A6
#define Encoder_1B 19 // A5
#define Encoder_2A 17 // A3
#define Encoder_2B 16 // A2

int counter1 = 0;
int counter2 = 0;
int currentState1 = 0;
int previousState1 = 0;
int currentState2 = 0;
int previousState2 = 0;


void setup() {
  pinMode(ServoFeedback_R, INPUT);
  pinMode(ServoFeedback_L, INPUT);
  pinMode(Encoder_1A, INPUT);
  pinMode(Encoder_1B, INPUT);
  pinMode(Encoder_2A, INPUT);
  pinMode(Encoder_2B, INPUT);  

  Serial.begin(19200);
  analogReadResolution(10);

  previousState1 = digitalRead(Encoder_1B);
  previousState2 = digitalRead(Encoder_2B);
}

void loop() {
  currentState1 = digitalRead(Encoder_1B);
  currentState2 = digitalRead(Encoder_2B);

  if(currentState1 != previousState1){
    if(digitalRead(Encoder_1A) != currentState1){
      counter1 --;
    }
    else{
      counter1 ++;
    }
  }

  if(currentState2 != previousState2){
    if(digitalRead(Encoder_2A) != currentState2){
      counter2 --;
    }
    else{
      counter2 ++;
    }
  }
  
  float volt_R = analogRead(ServoFeedback_R) * 3.3/1024;
  float volt_L = analogRead(ServoFeedback_L) * 3.3/1024;
  previousState1 = currentState1;
  previousState2 = currentState2;

  Serial.println(volt_R); 
  Serial.println(volt_L); 
  Serial.println(counter1/1000*360); 
  Serial.println(counter2/1000*360); 
  
  delay(100);
}
