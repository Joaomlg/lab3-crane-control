#include "StepMotor_28BYJ48.h"
#include <Arduino.h>

StepMotor_28BYJ48::StepMotor_28BYJ48(int pin1, int pin2, int pin3, int pin4, float externalEngineRatio=1) {
  this->controller = new Stepper(this->innerStepsPerRevolution, pin1, pin2, pin3, pin4);
  
  this->externalEngineRatio = externalEngineRatio;

  this->currentStep = 0;
  this->asyncRemainingSteps = 0;

  this->controller->setSpeed(this->rpmSpeed);

  this->pin1 = pin1;
  this->pin2 = pin2;
  this->pin3 = pin3;
  this->pin4 = pin4;
}

void StepMotor_28BYJ48::rotate(int steps) {
  this->controller->step(steps);
  this->currentStep += steps;
}

float StepMotor_28BYJ48::getCurrentDegreesPosition() {
  float currentDegreesPosition = this->stepsToDegrees(this->currentStep);
  float currentRevolutionDegreesPosition = fmod(currentDegreesPosition, this->degreesPerRevolution);
  
  if (currentDegreesPosition < 0) {
    return this->degreesPerRevolution + currentRevolutionDegreesPosition;
  }

  return currentRevolutionDegreesPosition;
}

void StepMotor_28BYJ48::rotateDegreesAsync(float deg) {
  int steps = this->degreesToSteps(deg);
  this->asyncRemainingSteps += abs(steps);
  this->rotateDirection = steps < 0 ? -1 : 1;
}

bool StepMotor_28BYJ48::isRotating() {
  return this->asyncRemainingSteps > 0;
}

void StepMotor_28BYJ48::loop() {
  if (this->asyncRemainingSteps == 0) {
    this->turnDown();
    return;
  }

  int steps = min(this->asyncStep, this->asyncRemainingSteps);

  this->rotate(steps * this->rotateDirection);

  this->asyncRemainingSteps -= steps;
}

void StepMotor_28BYJ48::turnDown() {
  digitalWrite(this->pin1, LOW);
  digitalWrite(this->pin2, LOW);
  digitalWrite(this->pin3, LOW);
  digitalWrite(this->pin4, LOW);
}

float StepMotor_28BYJ48::stepsToDegrees(int steps) {
  float degrees = steps / this->stepsPerDegree / this->externalEngineRatio;
  return degrees;
}

int StepMotor_28BYJ48::degreesToSteps(float deg) {
  int steps = round(this->externalEngineRatio * this->stepsPerDegree * deg);
  return steps;
}