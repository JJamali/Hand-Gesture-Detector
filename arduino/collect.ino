int Signal;

// The SetUp Function:
void setup() {
   Serial.begin(9600);         // Set's up Serial Communication at certain speed.
}

void loop() {

  Signal = analogRead(A0);
  Serial.println(Signal);
   
  delay(10);
}
