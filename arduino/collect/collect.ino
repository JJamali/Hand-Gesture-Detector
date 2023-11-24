/*
 * Anything that gets printed is sent to python
 * 
 * 
 */

const int sendPin = 9;  
const int echoPin = 10; 

const int horizontalMotorPin = 1;
const int verticalMotorPin = 2;

float duration, distance;

void setup() {  
  pinMode(sendPin, OUTPUT);  
  pinMode(echoPin, INPUT);  
  Serial.begin(9600);

  int ROWS = 6;
  int COLS = 10;
  int x = 0;
  int y = 0;
  bool hDirection = 1;
}  

void loop() {
  //take photo, then move
  
  readValue();
  moveHorizontal(hDirection, 1);

  if (x+1 == ROWS and y+1 == COLS){ //TODO fix this as end point could be at y = 0 instead of y = COLS - 1
    // if end of scan reached
    moveHorizontal(0, ROWS);
    moveVertical(0, COLS);
    exit(0); // end program
  }
  elif (x+1 == ROWS && hDirection || x == 0 && !hDirection){
    // if we've reached an edge of our grid, change direction and increment y
    hDirection = !hDirection;
    moveVertical(1, 1);
    y++
  }
}

// direction of 0 is left, 1 is right
void moveHorizontal(direction, pixels){

  // activate motor
  
  // increment/decrement x based on direction
  if (direction){
    x++
  }
  else {
    x--
  }
}

// direction of 0 is up, 1 is down
void moveVertical(direction, pixels){
  // activate motor
  y++
}

int readValue() {
  digitalWrite(sendPin, LOW);
  delayMicroseconds(2);
  digitalWrite(sendPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sendPin, LOW);

  // turn off arduino interrupts to increase accuracy of receiver
  noInterrupts();
  duration = pulseIn(echoPin, HIGH);
  interrupts();
  
  // 0.0343 is the speed sound travels in centimeters per microsecond
  distance = (duration*.0343)/2; 
  Serial.println(distance);
}
