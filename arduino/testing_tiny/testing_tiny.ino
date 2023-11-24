
const int stepsPerPixel = 73;  // change this to fit the number of steps per pixel

#include <TinyStepper.h>


// Initialize the TinyStepper Class
TinyStepper hStepper(4096, 8, 9, 10, 11);
//TinyStepper hStepper(4096, 4, 3, 5, 6);

const int horizontalMotorPin = 1;

float duration, distance;

int ROWS = 6;
int COLS = 10;
int x = 0;
int y = 0;
bool hDirection = true;

void setup() {  
//  pinMode(sendPin, OUTPUT);  
//  pinMode(echoPin, INPUT);  
  Serial.begin(9600);
  // set the speed at 60 rpm:
  hStepper.Enable();
  delay(1000);
//  hStepper.setSpeed(150);
  
}  

void loop() {
  // Random back and forth
  Serial.println("Random Test");
  hStepper.Move(45);
  hStepper.Move(-90);
  hStepper.Move(120);
  hStepper.Move(-15);
  hStepper.Move(30);
  delay(2000);
}

// direction of 0 is left, 1 is right
void moveHorizontal(bool direction, int pixels){
//  if (!direction){
//    pixels *= -1;
//  }
//  Serial.println(stepsPerPixel * pixels);
//  // activate motor
//  hStepper.step(stepsPerPixel * pixels);
////  delay(500);  

}
