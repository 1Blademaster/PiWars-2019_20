#include <MPU6050_tockn.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1351.h>
#include <SPI.h>

#define SCREEN_WIDTH  128
#define SCREEN_HEIGHT 96

#define SCLK_PIN 7
#define MOSI_PIN 3
#define DC_PIN   4
#define CS_PIN   5
#define RST_PIN  6

#define BLACK           0x0000
#define BLUE            0x001F
#define RED             0xF800
#define GREEN           0x07E0
#define CYAN            0x07FF
#define MAGENTA         0xF81F
#define YELLOW          0xFFE0  
#define WHITE           0xFFFF

Adafruit_SSD1351 screen = Adafruit_SSD1351(SCREEN_WIDTH, SCREEN_HEIGHT, CS_PIN, DC_PIN, MOSI_PIN, SCLK_PIN, RST_PIN); 
MPU6050 mpu6050(Wire);

void setup() {
  Serial.begin(9600);
  screen.begin();
  screen.fillScreen(0);
  screen.setTextSize(2);
  Wire.begin();
  mpu6050.begin();
  screen.setCursor(1, 40);
  screen.println("Setting up...");
  mpu6050.calcGyroOffsets(true);
  delay(100);
  screen.fillScreen(0);
}

void loop() {
  mpu6050.update();
  screen.setCursor(1, 20);
  screen.println("x: " + String(mpu6050.getAngleX(), 3));
  Serial.print("x: " + String(mpu6050.getAngleX()));
  screen.setCursor(1, 40);
  screen.println("y: " + String(mpu6050.getAngleY(), 3));
  Serial.print("y: " + String(mpu6050.getAngleY()));
  screen.setCursor(1, 60);
  screen.println("z: " + String(mpu6050.getAngleZ(), 3));
  Serial.print("z: " + String(mpu6050.getAngleZ()));
  screen.fillScreen(0);
}
