#include <Wire.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <U8g2lib.h>
#include <WiFiUdp.h>
#include <NTPClient.h>

// Replace with your Wi-Fi credentials and Django API details
const char* ssid = "Ellis";
const char* password = "bhfn13011";
const char* username = "group3";
const char* user_password = "group3";
const char* token_url = "https://zunzun.pythonanywhere.com/api/token/";
const char* djangoAPIUrl = "http://zunzun.pythonanywhere.com/api/activities/";
unsigned long lastDisplayUpdate = 0;

boolean fireAlarmReported = false;

// OLED SSD1306 display pins
#define OLED_SDA 4
#define OLED_SCL 15
#define OLED_RST 16

WiFiClient espClient;

// Button configuration
const int buttonPin = 0;
int buttonState = 0;

// U8g2 OLED display configuration
U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ OLED_RST, /* clock=*/ OLED_SCL, /* data=*/ OLED_SDA);

// NTPClient configuration
WiFiUDP ntpUDP;
int timeZoneOffset = 25200; // Bangkok, Thailand time zone offset in seconds (7 hours)
NTPClient timeClient(ntpUDP, "pool.ntp.org", timeZoneOffset);


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

void sendDataToDjangoAPI(String jwt_token, double lat, double lon){
  HTTPClient http;
  http.begin(djangoAPIUrl);
  http.addHeader("Authorization", "Bearer " + jwt_token);
  http.addHeader("Content-Type", "application/json; charset=UTF-8");
  
  String json_data = "{\"worker_id\":\"W001\",\"lat\":" + String(lat, 6) + ",\"lon\":" + String(lon, 6) + ",\"emergency_case\":2}";
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

  // Set fireAlarmReported to true if the response code is 201 (created) or 200 (OK)
  if (httpResponseCode == 201 || httpResponseCode == 200) {
    fireAlarmReported = true;
  }

  http.end();
}

void drawFireText() {
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_ncenB14_tr); // Choose a suitable font
  u8g2.setDrawColor(1); // Set draw color to red
  u8g2.drawStr(20, 50, "FIRE "); // Draw "FIRE" in the middle of the screen
  u8g2.sendBuffer();
}

void drawFireAlarmOn() {
  u8g2.clearBuffer();
  u8g2.setDrawColor(1);
  u8g2.drawBox(0, 0, 128, 64); // Draw a red background
  u8g2.setDrawColor(0);
  u8g2.setFont(u8g2_font_ncenB14_tr); // Choose a suitable font
  u8g2.drawStr(0, 32, "Fire case"); // Draw "Fire case" with white text and red background
  u8g2.setDrawColor(2);
  u8g2.drawStr(0, 64, "reported");
  u8g2.sendBuffer();
}

void drawTime() {
  timeClient.update();
  String formattedTime = timeClient.getFormattedTime();
  u8g2.setFont(u8g2_font_6x10_tf); // Choose a suitable font for the time display
  u8g2.setDrawColor(1); // Set draw color to white
  u8g2.drawStr(40, 10, formattedTime.c_str());
  u8g2.sendBuffer();
}

void drawFireCaseReported() {
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_6x10_tr); // Choose a suitable font
  u8g2.drawStr(0, 32, "Fire case");
  u8g2.drawStr(0, 48, "reported");
  u8g2.sendBuffer();
}

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);

  // Initialize the OLED display
  u8g2.begin();

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to Wi-Fi");

  // Initialize NTP client
  timeClient.begin();
}


void loop() {

  unsigned long currentTime = millis();
  
  if (currentTime - lastDisplayUpdate >= 1000) {
    drawTime();
    lastDisplayUpdate = currentTime;
  }
  buttonState = digitalRead(buttonPin);

  Serial.flush();

  if (buttonState == LOW) {

    // Clear the display and set the font
    u8g2.clearBuffer();
    u8g2.setFont(u8g2_font_ncenB14_tr); // Choose a font that fits your needs

    // Display "FIRE ALARM ON" with a red background
    u8g2.setDrawColor(1); // Set draw color to white
    u8g2.drawStr(15, 40, "FIRE");
    u8g2.drawStr(0, 64, "ALARM ON");
    u8g2.sendBuffer();
    drawTime(); // Display the current time at the bottom of the screen

    double lat = 0.0;
    double lon = 0.0;

    Serial.print("Latitude: ");
    Serial.println(lat, 6);
    Serial.print("Longitude: ");
    Serial.println(lon, 6);

    String jwtToken = getJWTToken();
    if (jwtToken != "") {
      Serial.println("Calling sendDataToDjangoAPI...");
      Serial.flush();
      sendDataToDjangoAPI(jwtToken, lat, lon);
      drawFireCaseReported(); // Show the "Fire case reported" text when the button is pressed
      drawTime(); // Display the current time at the bottom of the screen
    } else {
      Serial.println("JWT token is empty!");
      Serial.flush();
    }
  } else {
    if (fireAlarmReported) {
      // Display "Fire alarm was reported" text
      u8g2.clearBuffer();
      u8g2.setFont(u8g2_font_ncenB14_tr);
      u8g2.drawStr(10, 31, "Fire Alarm");
      u8g2.drawStr(20, 60, "reported");
      u8g2.sendBuffer();
    } else {
      // Clear the display and set the font
      u8g2.clearBuffer();
      u8g2.setFont(u8g2_font_ncenB18_tr);
      u8g2.drawStr(25, 40, "FIRE");
      u8g2.setFont(u8g2_font_ncenB12_tr);
      u8g2.drawStr(5, 55, "Hayman");
      u8g2.sendBuffer();
    }
    drawTime(); // Display the current time at the bottom of the screen
  }

  delay(100);
}
