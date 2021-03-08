/*
  Fade

  This example shows how to fade an LED on pin 9 using the analogWrite()
  function.

  The analogWrite() function uses PWM, so if you want to change the pin you're
  using, be sure to use another PWM capable pin. On most Arduino, the PWM pins
  are identified with a "~" sign, like ~3, ~5, ~6, ~9, ~10 and ~11.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Fade
*/

int led = 9;           // the PWM pin the LED is attached to

// the setup routine runs once when you press reset:
void setup() {
  Serial.begin(9600);
  // declare pin 9 to be an output:
  pinMode(led, OUTPUT);
}

int ON = 255;
int OFF = 0;

void blink_one()
{
  analogWrite(led, ON);
  delay(500);
  analogWrite(led, OFF);
  delay(200);
}

void blink_single_digit(int number)
{
  Serial.print("printing digit: ");
  Serial.println(number);
    while (number) {
      blink_one();
      number = number - 1;
    }
    delay(1000);
}

void loop() {
  blink_single_digit(2);
  blink_single_digit(4);
  blink_single_digit(3);
}
