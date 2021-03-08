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

/* https://en.wikipedia.org/wiki/Morse_code */

int alphabet[5][4] = {
  /* a */ {1,2,0,0},
  /* b */ {2,1,1,1},
  /* c */ {2,1,2,1},
  /* d */ {2,1,1,0},
  /* e */ {1,0,0,0}
};

void blink_short()
{
  analogWrite(led, ON);
  delay(200);
  analogWrite(led, OFF);
  delay(300);
}

void blink_long()
{
  analogWrite(led, ON);
  delay(500);
  analogWrite(led, OFF);
  delay(300);
}

void blink_single_letter(char letter)
{
  Serial.print("printing letter: ");
  Serial.println(letter);
  int n = letter - 'a';
  int i;
  for (i=0;i<4;i++) {
    if (alphabet[n][i] == 1) {
      blink_short();
    }
    else if (alphabet[n][i] == 2) {
      blink_long();
    }
  }
  delay(1000);
}

void blink_word(const char *str)
{
  Serial.print("printing word: ");
  Serial.println(str);
  int i;
  for (i=0;i<strlen(str);i++) {
     blink_single_letter(str[i]);
  }
}

// the loop routine runs over and over again forever:
void loop() {
  blink_word("dad");
  blink_single_letter('a');
  blink_single_letter('b');
  blink_single_letter('c');
  blink_single_letter('d');
  blink_single_letter('e');
}
