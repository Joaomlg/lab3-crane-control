#ifndef STEP_MOTOR_H
#define STEP_MOTOR_H

#include <Arduino.h>
#include <Stepper.h>
#include <math.h>

class StepMotor_28BYJ48 {
  public:
    StepMotor_28BYJ48(int pin1, int pin2, int pin3, int pin4, float externalEngineRatio=1);
    
    void setInitialPosition(float initialPosition);
    void rotate(int steps);
    float getCurrentRelativeDegreesPosition();
    float getCurrentDegreesPosition();
    void rotateDegreesAsync(float deg);
    bool isRotating();
    void loop();
    void turnDown();

    int pin1;
    int pin2;
    int pin3;
    int pin4;

  private:
    Stepper* controller;

    int currentStep;
    float externalEngineRatio;
    float asyncRemainingSteps;
    int rotateDirection;

    const int innerStepsPerRevolution = 64;
    const int outerStepsPerRevolution = 2048;
    const int degreesPerRevolution = 360;
    const float stepsPerDegree = (float) outerStepsPerRevolution / degreesPerRevolution;
    
    const int rpmSpeed = 200;
    const float asyncStep = 5;

    float stepsToDegrees(int steps);
    int degreesToSteps(float deg);
};

#endif