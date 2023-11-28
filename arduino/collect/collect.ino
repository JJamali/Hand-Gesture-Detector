#include <TinyStepper.h>

//6 and 10
const int stepsPerPixel = 105;  // change this to fit the number of steps per pixel 169
const int stepsPerPixelH = 80;

TinyStepper vStepper(4096, 8, 9, 10, 11);
TinyStepper hStepper(4096, 4, 5, 3, 6);

const int sendPin = 7;  
const int echoPin = 2; 

float duration, distance;

int ROWS = 12; //6
int COLS = 14; //10
int x = 0;
int y = 0;
bool hDirection = 1;

void setup() {  
  delay(10000);
  pinMode(sendPin, OUTPUT);  
  pinMode(echoPin, INPUT);  

  hStepper.Enable();
  vStepper.Enable();
  Serial.begin(9600);
  
}  

void loop() {
  //take photo, then move
  readValue();
  moveHorizontal(hDirection, 1);
  // code with assumption of even rows

//  if (y == COLS and (ROWS % 2 == 0 and x == 0 or ROWS % 2 == 1 and x == COLS - 1)

  if (y == ROWS){
    // we check if its odd or even to determine ending location
    // end scan - reset sensor
//    moveHorizontal(!hDirection, COLS);
    moveVertical(0, ROWS - 1);
    Serial.println("done");
    exit(0); // end program
  }
  else if (hDirection && x == COLS || !hDirection && x == 0){ //changed first x from ROWS
    // if we've reached an edge of our grid, change direction and increment y
    hDirection = !hDirection;
    moveVertical(1, 1);
    Serial.println("nr");
  }
}

// direction of 0 is left, 1 is right
void moveHorizontal(bool direction, int pixels){
  if (!direction){
    pixels *= -1;
  }
  
  // activate motor
  hStepper.Move(stepsPerPixelH * pixels);
  delay(500);  
  
  // increment/decrement x based on direction
  if (direction){
    x++;
  }
  else {
    x--;
  }
}

// direction of 0 is up, 1 is down
void moveVertical(bool direction, int pixels){

  if (!direction){
    pixels *= -1;
  }
  
  // activate motor
  vStepper.Move(stepsPerPixel * pixels);
  delay(500);  
  y++;
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
  delay(50);
}
