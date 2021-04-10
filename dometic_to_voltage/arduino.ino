/*
 * Copyright 2021 Ilker Temir <ilker@ilkertemir.com>
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

int greenPin = 2;      // Green line from tank sensor
int orangePin = 5;     // Orange line from tank sensor
int redPin = 8;        // Red line from tank sensor
int outputPin = 11;    // Output to Pico for voltage based reads
int green = HIGH;
int orange = HIGH;
int red = HIGH;
int outputValue = 0;

void setup() {
  pinMode(greenPin, INPUT_PULLUP);
  pinMode(orangePin, INPUT_PULLUP);
  pinMode(redPin, INPUT_PULLUP);
}

void loop() {
  green = digitalRead(greenPin);
  orange = digitalRead(orangePin);
  red = digitalRead(redPin);

  outputValue = 33;
  if (green == LOW) {
    outputValue = 0;
  }
  else if (red == LOW) {
    outputValue = 100;
  }
  else if (orange == LOW) {
    outputValue = 66;
  }
  analogWrite(outputPin,outputValue);
}
