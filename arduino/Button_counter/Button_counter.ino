/*
  Button_counter - keep track of how many times the button is pushed.
  Based on Button, http://www.arduino.cc/en/Tutorial/Button
*/

// constants won't change. They're used here to set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int counter = 0;

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void flash_n_times(int n)
{
  while (n > 0) {
    digitalWrite(ledPin, HIGH);
    delay(200);
    digitalWrite(ledPin, LOW);
    delay(200);
    n = n -1;
  }
}

void loop() {
  int reading = digitalRead(buttonPin);
  if (reading != buttonState) {
    buttonState = reading;
    if (buttonState == HIGH) {
      flash_n_times(1);
    }
    else {
      counter = counter + 1;
      /* limit to 4, then go back to 1 */
      if (counter > 4) counter = 1;
      flash_n_times(counter);
    }
  }
}
