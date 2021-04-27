/*
  Button_count_input - count how many times the button is pushed, then flash back that number.
  Based on Button, http://www.arduino.cc/en/Tutorial/Button
*/

#include "pitches.h"

// constants won't change. They're used here to set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
int buttonCount = 0;         // variable for debouncing pushbutton
int counter = 0;             // number of flashes

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

int notes[][2] = {
{NOTE_A4, 8}, /* eigth note */
{NOTE_C4, 8},
{NOTE_D4, 4}, /* quarter note */
{NOTE_D4, 4},
{NOTE_D4, 8},
{NOTE_E4, 8},
{NOTE_F4, 4},
{NOTE_F4, 4},
{NOTE_F4, 8},
{NOTE_G4, 8},
{NOTE_E4, 4},
{NOTE_E4, 4},
{NOTE_D4, 8},
{NOTE_C4, 8},
{NOTE_D4, 4},
{NOTE_D4, 4},
{0, 1} /* whole rest */
};

void play_tune(void)
{
  for (int thisNote = 0; thisNote < sizeof(notes)/sizeof(notes[0]); thisNote++) {
    // to calculate the note duration, take one second divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / notes[thisNote][1];
    tone(8, notes[thisNote][0], noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(8);
  }
}

void loop() {
  int reading = digitalRead(buttonPin);
  Serial.print("reading: ");
  Serial.print(reading);
  Serial.println("");

  // debouce it
  if (reading != buttonState) {
    buttonState = reading;
    buttonCount = 0;
  }
  else {
    buttonCount += 1;
  }
  
  if (buttonState == HIGH && buttonCount == 5) {
    Serial.print("play ");
    Serial.println(counter);
    counter += 1;
    flash_n_times(counter);
    play_tune();
  }
}
