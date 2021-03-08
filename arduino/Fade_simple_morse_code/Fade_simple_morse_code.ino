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
int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by

// the setup routine runs once when you press reset:
void setup() {
  // declare pin 9 to be an output:
  pinMode(led, OUTPUT);
}

int short_time = 100;
int long_time = 500;
int interval_time = 200;
int letter_interval_time = 800;

void show_symbol(int t)
{
  analogWrite(led, 255);
  delay(t);
  analogWrite(led, 0);
  delay(interval_time);
}

void show_letter(char ch)
{
   if (ch == 's') {
       show_symbol(short_time);
       show_symbol(short_time);
       show_symbol(short_time);
   }
   else if (ch == 'o') {
       show_symbol(long_time);
       show_symbol(long_time);
       show_symbol(long_time);
   }
   delay(interval_time);
}

// the loop routine runs over and over again forever:
void loop() {
  // set the brightness of pin 9:

  show_letter('s');
  show_letter('o');
  show_letter('s');

  delay(letter_interval_time);
  delay(letter_interval_time);
}
