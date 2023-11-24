#include <Stepper.h> //if no work use tinystepper

const int stepsPerPixel = 73;  // change this to fit the number of steps per pixel

// initialize the stepper library on pins 8 through 11. First one isn't PWM:
Stepper hStepper(stepsPerPixel, 8, 9, 10, 11);

const int horizontalMotorPin = 1;
const int verticalMotorPin = 2;

float duration, distance;

int ROWS = 6;
int COLS = 10;
int x = 0;
int y = 0;
bool hDirection = true;

void setup() {  
//  pinMode(sendPin, OUTPUT);  
//  pinMode(echoPin, INPUT);  

  // set the speed at 60 rpm:
  hStepper.setSpeed(150);
  Serial.begin(9600);
}  

void loop() {
//  moveHorizontal(hDirection, 11);
//  delay(3000);
//  moveHorizontal(!hDirection, 11);
  hStepper.step(500);
  delay(20000);
  hStepper.step(-500);
}

// direction of 0 is left, 1 is right
void moveHorizontal(bool direction, int pixels){
  if (!direction){
    pixels *= -1;
  }
  Serial.println(stepsPerPixel * pixels);
  // activate motor
  hStepper.step(stepsPerPixel * pixels);
//  delay(500);  

}
