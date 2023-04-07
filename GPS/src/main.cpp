#include <Wire.h>
#include <TinyGPS++.h>
#include <HardwareSerial.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>


// Replace with your Wi-Fi credentials and Django API details
const char* ssid = "Ellis";
const char* password = "bhfn13011";
const char* username = "group3";
const char* user_password = "group3";
const char* api_url = "http://zunzun.pythonanywhere.com/api/activities/";
const char* token_url = "https://zunzun.pythonanywhere.com/api/token/";
const char* deviceID = "W001";
const char* djangoAPIUrl = "http://zunzun.pythonanywhere.com/api/activities/";




HardwareSerial GPS_Serial(1);
TinyGPSPlus gps;


WiFiClient espClient;


// Button configuration
const int buttonPin = 39;
int buttonState = 0;
unsigned long previousMillis = 0;

String getJWTToken() {
 HTTPClient http;
 http.begin(token_url);
 http.addHeader("Content-Type", "application/json");
 String json_data = "{\"username\":\"" + String(username) + "\",\"password\":\"" + String(user_password) + "\"}";
 int httpResponseCode = http.POST(json_data);


 Serial.println("Getting JWT token...");
 Serial.flush();


 if (httpResponseCode > 0) {
   String payload = http.getString();
   Serial.print("Payload: ");
   Serial.println(payload); // Add this line to print the payload
   int start_pos = payload.indexOf("\"access\":\"") + 10;
   int end_pos = payload.indexOf("\"", start_pos + 1);
   String jwt_token = payload.substring(start_pos, end_pos);
   Serial.print("JWT token: ");
   Serial.println(jwt_token); // Add this line to print the JWT token
   Serial.flush();
   return jwt_token;
 } else {
   Serial.print("Error on getting JWT token: ");
   Serial.println(httpResponseCode);
   Serial.flush();
   return "";
 }
 http.end();
}


void sendDataToDjangoAPI(String jwt_token, double lat, double lon, int emergency_case) { // Modify this line to add emergency_case parameter



 HTTPClient http;
 http.begin(djangoAPIUrl);
 http.addHeader("Authorization", "Bearer " + jwt_token);
 http.addHeader("Content-Type", "application/json; charset=UTF-8");
  String json_data = "{\"worker_id\":\"W001\",\"lat\":" + String(lat, 6) + ",\"lon\":" + String(lon, 6) + ",\"emergency_case\":" + String(emergency_case) + "}"; // Modify this line to use emergency_case parameter
 http.addHeader("Content-Length", String(json_data.length()));


 Serial.print("JSON data: ");
 Serial.println(json_data);
  Serial.print("Authorization header: ");
 Serial.println("Bearer " + jwt_token);
 Serial.print("Content-Type header: ");
 Serial.println("application/json");
  Serial.println("Sending data to Django API...");
 int httpResponseCode = http.POST(json_data);
 Serial.print("Data sent to Django API. Response code: ");
 Serial.println(httpResponseCode);


 String responsePayload = http.getString();
 Serial.print("Response payload: ");
 Serial.println(responsePayload);


 http.end();
}


void setup() {
 Serial.begin(115200);
 GPS_Serial.begin(9600, SERIAL_8N1, 12, 15); // RX=12, TX=15
 pinMode(buttonPin, INPUT_PULLUP);


 // Connect to Wi-Fi
 WiFi.begin(ssid, password);
 while (WiFi.status() != WL_CONNECTED) {
   delay(500);
   Serial.print(".");
 }
 Serial.println("Connected to Wi-Fi");
}


void loop() {
  // Read GPS data
  while (GPS_Serial.available() > 0) {
    gps.encode(GPS_Serial.read());
  }

  // Check button state
  buttonState = digitalRead(buttonPin);

  // Check if 3 minutes have passed or the button is pressed
  unsigned long currentMillis = millis();
  bool timePassed = (currentMillis - previousMillis) >= (15 * 1000);
  if (timePassed || buttonState == LOW) {
    previousMillis = currentMillis;

    if (gps.location.isUpdated()) {
      Serial.print("Latitude: ");
      Serial.println(gps.location.lat(), 6);
      Serial.print("Longitude: ");
      Serial.println(gps.location.lng(), 6);
    }

    if (gps.location.isValid()) {
      String jwtToken = getJWTToken();
      if (jwtToken != "") {
        Serial.println("Calling sendDataToDjangoAPI...");
        Serial.flush();
        sendDataToDjangoAPI(jwtToken, gps.location.lat(), gps.location.lng(), buttonState == LOW ? 1 : 0); // Modify this line to pass emergency_case value based on the condition
      } else {
        Serial.println("JWT token is empty!");
        Serial.flush();
      }
    } else {
      Serial.println("GPS location is not valid!");
      Serial.flush();
    }
  }

  delay(100);
}
