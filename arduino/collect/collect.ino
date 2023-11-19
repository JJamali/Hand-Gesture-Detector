const int trigPin = 9;  
const int echoPin = 10; 

float duration, distance;

void setup() {  
  pinMode(trigPin, OUTPUT);  
  pinMode(echoPin, INPUT);  
  Serial.begin(9600);
}  

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  //turn off arduino interrupts to increase accuracy of receiver
  noInterrupts();
  duration = pulseIn(echoPin, HIGH);
  interrupts();
  
  //0.0343 is the speed sound travels in centimeters per microsecond
  distance = (duration*.0343)/2; 
  Serial.println(distance);
}
