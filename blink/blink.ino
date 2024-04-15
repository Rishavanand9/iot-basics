// Arduino Sketch
int ledPin = 13; // Pin where the LED is connected

void setup() {
  pinMode(ledPin, OUTPUT); // Set the LED pin as output
  Serial.begin(9600); // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) { // Check if there is an incoming data
    char command = Serial.read(); // Read the incoming byte
    if (command == 'H') {
      digitalWrite(ledPin, HIGH); // Turn LED on
    } else if (command == 'L') {
      digitalWrite(ledPin, LOW); // Turn LED off
    }
  }
}
