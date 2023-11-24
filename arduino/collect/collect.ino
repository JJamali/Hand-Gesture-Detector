#include <Stepper.h>

const int stepsPerPixel = 20;  // change this to fit the number of steps per pixel

// initialize the stepper library on pins 8 through 11. First one isn't PWM:
Stepper hStepper(stepsPerPixel, 8, 9, 10, 11);
// initialize the stepper library on pins 3 through 6. First one isn't PWM:
Stepper vStepper(stepsPerPixel, 4, 3, 5, 6);


const int sendPin = 9;  
const int echoPin = 10; 

const int horizontalMotorPin = 1;
const int verticalMotorPin = 2;

float duration, distance;

int ROWS = 6;
int COLS = 10;
int x = 0;
int y = 0;
bool hDirection = 1;

void setup() {  
  pinMode(sendPin, OUTPUT);  
  pinMode(echoPin, INPUT);  

  // set the speed at 60 rpm:
  hStepper.setSpeed(60);
  Serial.begin(9600);
}  

void loop() {
  //take photo, then move
  readValue();
  moveHorizontal(hDirection, 1);

  if (y+1 == COLS and (ROWS % 2 == 0 and x == 0 or ROWS % 2 == 1 and x == COLS - 1)){
    // we check if its odd or even to determine ending location
    // end scan - reset sensor
    moveHorizontal(0, ROWS);
    moveVertical(0, COLS);
    exit(0); // end program
  }
  else if (x+1 == ROWS && hDirection || x == 0 && !hDirection){
    // if we've reached an edge of our grid, change direction and increment y
    hDirection = !hDirection;
    moveVertical(1, 1);
    y++;
  }
}

// direction of 0 is left, 1 is right
void moveHorizontal(bool direction, int pixels){
  if (!direction){
    pixels *= -1;
  }
  
  // activate motor
  hStepper.step(stepsPerPixel * pixels);
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
  vStepper.step(stepsPerPixel * pixels);
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
}
