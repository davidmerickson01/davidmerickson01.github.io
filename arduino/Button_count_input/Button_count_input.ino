/*
  Button_count_input - count how many times the button is pushed, then flash back that number.
  Based on Button, http://www.arduino.cc/en/Tutorial/Button
*/

// constants won't change. They're used here to set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int counter = 0;
unsigned long press_time = 0;

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void flash_n_times(int n)
{
  while (n > 0) {
    digitalWrite(ledPin, HIGH);
    delay(100);
    digitalWrite(ledPin, LOW);
    delay(100);
    n = n -1;
  }
}

void loop() {
  int reading = digitalRead(buttonPin);
  if (reading != buttonState) {
    buttonState = reading;
    if (buttonState == HIGH) {
      press_time = millis();
      digitalWrite(ledPin, HIGH);
      delay(100);
      digitalWrite(ledPin, LOW);
      counter = counter + 1;
      Serial.println("press");
    }
  }
  else {
    unsigned long dur = millis() - press_time;
    if (reading == LOW && press_time > 0 && dur > 1000) {
      Serial.print("flash ");
      Serial.println(counter);
      press_time = 0;
      flash_n_times(counter);
      counter = 0;
    }
  }
}
