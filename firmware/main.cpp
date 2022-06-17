#include "StepMotor_28BYJ48.h"

#include <Arduino.h>
#include <Ultrasonic.h>

const float spearExternalEngineRatio = 3.35;
StepMotor_28BYJ48 spear(8, 10, 9, 11, spearExternalEngineRatio);

const float applianceExternalEngineRatio = 1 / (5 * PI);
StepMotor_28BYJ48 appliance(2, 4, 3, 5, applianceExternalEngineRatio);

const int trigPin = 6;
const int echoPin = 7;
Ultrasonic distanceSensor(trigPin, echoPin);
unsigned int currentDistance = 0;

const int magnetPin = 12;
const int magnetHighStatus = LOW;
int magnetStatus = !magnetHighStatus;

unsigned long previousMillis = 0;
const long serialWriteInterval = 1000;

void setup() {
  pinMode(magnetPin, OUTPUT);
  digitalWrite(magnetPin, magnetStatus);

  Serial.begin(9600);
}

void processCommand() {
  if (!Serial.available()) {
    return;
  }

  String data = Serial.readString();

  if (data.startsWith("spear:set:")) {
    float deg = data.substring(10).toFloat();
    spear.rotateDegreesAsync(deg);
    return;
  }

  if (data.startsWith("appliance:set:")) {
    float deg = data.substring(14).toFloat();
    appliance.rotateDegreesAsync(deg);
    return;
  }

  if (data.startsWith("magnet:set:")) {
    int status = data.substring(11).toInt();
    magnetStatus = status ? magnetHighStatus : !magnetHighStatus;
    digitalWrite(magnetPin, magnetStatus);
    return;
  }
}

bool shouldTelemetry() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis < serialWriteInterval) {
    return false;
  }

  previousMillis = currentMillis;
  
  return true;
}

void telemetry() {
  Serial.print(spear.getCurrentDegreesPosition());
  Serial.print(":");
  Serial.print(appliance.getCurrentDegreesPosition());
  Serial.print(":");
  Serial.print(magnetStatus == magnetHighStatus);
  Serial.print(":");
  Serial.println(currentDistance);
}

void loop() {
  if (!spear.isRotating() && !appliance.isRotating()) {
    processCommand();
  }

  spear.loop();
  appliance.loop();

  if (shouldTelemetry()) {
    currentDistance = distanceSensor.read();
    telemetry();
  } else {
    delay(2);
  }
}