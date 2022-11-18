#include <IRremote.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int IRPIN = 11;
IRrecv irrecv(IRPIN);
decode_results result;
int button = 0;
void setup()
{
  lcd.backlight();
  lcd.init();
  Serial.begin(9600);
  Serial.println("IRin: LOAD...");
  irrecv.enableIRIn();
  Serial.println("IRin: ONLINE");
  Initialize_streamer();
  lcd.setCursor(0, 0);
  lcd.print("IR Hexa decoder.");
  lcd.setCursor(0, 1);
  lcd.print("IR Hex:");
}
void loop() 
{
  if (irrecv.decode(&result)) 
  {
    button = button+1;
    Serial.print("Value: ");
    Serial.println(result.value, HEX);
    Write_streamer();
    irrecv.resume();
    lcd.setCursor(8, 1);
    lcd.print(result.value, HEX);
  }
  delay(500);
}
void Initialize_streamer()
{
Serial.println("The IRin is online."); //It's enabled
Serial.println("Press a Button"); //To start
}
void Write_streamer()
  { 
    Serial.print(result.value); //Store date on Arduino
    Serial.print(","); //Move to next column using a ","
    Serial.print(button); //Store date on Excel
    Serial.print(","); //Move to next column using a ","
    Serial.println(); //End of Row move to next row
  }
