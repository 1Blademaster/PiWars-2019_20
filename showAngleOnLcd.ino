#include <MPU6050_tockn.h>
#include <Wire.h>
#include<LiquidCrystal.h>

LiquidCrystal lcd(8,9,10,11,12,13);
MPU6050 mpu6050(Wire);

long timer = 0;

void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
  lcd.print("Starting Program");
  delay(1000);
  lcd.clear();
  delay(100);
  
}

void loop() {
  mpu6050.update();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("X     Y     Z");
  lcd.setCursor(0, 1);
  lcd.print(mpu6050.getAngleX());
  Serial.print("angleX : ");Serial.print(mpu6050.getAngleX());
  lcd.setCursor(6, 1);
  lcd.print(mpu6050.getAngleY());
  Serial.print("\tangleY : ");Serial.print(mpu6050.getAngleY());
  lcd.setCursor(12, 1);
  lcd.print(mpu6050.getAngleZ());
  Serial.print("\tangleZ : ");Serial.println(mpu6050.getAngleZ());
  delay(250);
}
