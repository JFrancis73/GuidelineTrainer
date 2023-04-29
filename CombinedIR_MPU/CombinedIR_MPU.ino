 #include "Wire.h"
 #include <MPU6050_light.h>
 MPU6050 mpu(Wire);
 unsigned long timer = 0;
 int IRSensor = 9; // connect IR sensor module to Arduino pin D9
 int LED = 13; // connect LED to Arduino pin 13
 int sensorStatus = LOW; //NO OBSTACLE
 void setup() {
   Serial.begin(9600);
   Wire.begin();
   pinMode(IRSensor, INPUT); // IR Sensor pin INPUT
   pinMode(LED, OUTPUT); // LED Pin Output
   byte status = mpu.begin();
   Serial.print(F("MPU6050 status: "));
   Serial.println(status);
   while (status != 0) { } // stop everything if could not connect to MPU6050
 Serial.println(F("Calculating offsets, do not move MPU6050"));
   delay(1000);
   mpu.calcOffsets(); // gyro and accelero
   Serial.println("Done!\n");
 }
 void loop() {
   mpu.update();
   int Init_z = mpu.getAngleZ();
 if ((millis() - timer) > 250) { // print data every 10ms
     int sensorStatusInt = 0;
     sensorStatus = digitalRead(IRSensor); // Set the GPIO as Input
      if (sensorStatus == HIGH) // Check if the pin high or not
      {
        // if the pin is high turn off the onboard Led
        digitalWrite(LED, HIGH); // LED LOW
        sensorStatusInt = 0;
        Serial.print("[0, " + String(mpu.getAngleZ()) + "]");
        Serial.println();
      }
      else  {
        //else turn on the onboard LED
        digitalWrite(LED, LOW); // LED High
        sensorStatusInt = 1;
        Serial.print("[1, " + String(mpu.getAngleZ()) + "]");
        Serial.println();
      }
     
     timer = millis();
   }
 }
