/*
  Melody
  Plays a melody

  created 4/13/21 by David Erickson
  Based on toneMelody by Tom Igoe, see http://www.arduino.cc/en/Tutorial/Tone
 
*/

#include "pitches.h"

/*
A two-dimensional array allows the pitch and the duration for each note to be on the same line
This makes adding more notes much easier.

Use like this:
notes[thisNote][0] = pitch
notes[thisNote][1] = duration

This melody is Pirates of the Caribbean from https://www.pinterest.com/pin/43910165092093671/
*/
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

void setup() {
}

void loop() {
  // iterate over the notes of the melody:
  
  // sizeof(notes) == the size of the whole array in bytes
  // sizeof(notes[0]) == the size of one element in the array in bytes
  // therefore, sizeof(notes)/sizeof(notes[0]) is the number of elements in the array (not bytes)
  
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
