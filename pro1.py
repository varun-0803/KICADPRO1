// Software simulation of 555 timer LED flasher using Arduino
int ledPin = 13; // Built-in LED or connect externally to pin 13

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH); // LED ON
  delay(500);                 // ON for 500 ms
  digitalWrite(ledPin, LOW);  // LED OFF
  delay(500);                 // OFF for 500 ms
}
