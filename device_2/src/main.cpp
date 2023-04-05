#include <Wire.h>
#include <TinyGPS++.h>
#include <HardwareSerial.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>


// Replace with your Wi-Fi credentials and MQTT broker details
const char* ssid = "Ellis";
const char* password = "bhfn13011";
const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;




const char* pub_topic = "ict720/ellis/data";
const char* sub_topic = "ict720/ellis/cmd";




HardwareSerial GPS_Serial(1);
TinyGPSPlus gps;


WiFiClient espClient;
PubSubClient client(espClient);


// Button configuration
const int buttonPin = 39;
int buttonState = 0;


void callback(char* topic, byte* payload, unsigned int length) {
 Serial.print("Message arrived [");
 Serial.print(topic);
 Serial.print("] ");
 for (unsigned int i = 0; i < length; i++) {
   Serial.print((char)payload[i]);
 }
 Serial.println();
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


 // Configure MQTT client
 client.setServer(mqtt_server, mqtt_port);
 client.setCallback(callback);
}


void loop() {
 // Read GPS data
 while (GPS_Serial.available() > 0) {
   gps.encode(GPS_Serial.read());
 }


 // Check button state
 buttonState = digitalRead(buttonPin);


 if (buttonState == LOW) {
   if (gps.location.isUpdated()) {
     Serial.print("Latitude: ");
     Serial.println(gps.location.lat(), 6);
     Serial.print("Longitude: ");
     Serial.println(gps.location.lng(), 6);
   }


   if (gps.location.isValid()) {
     // Connect to MQTT broker
     while (!client.connected()) {
       Serial.print("Attempting MQTT connection...");
       if (client.connect("TTGO_TBeam")) {
         Serial.println("connected");
         client.subscribe(sub_topic);
       } else {
         Serial.print("failed, rc=");
         Serial.print(client.state());
         Serial.println(" try again in 5 seconds");
         delay(5000);
       }
     }


     // Create JSON object
     StaticJsonDocument<100> doc;
     doc["latitude"] = gps.location.lat();
     doc["longitude"] = gps.location.lng();
     char jsonBuffer[100];
     serializeJson(doc, jsonBuffer);


     // Publish JSON to MQTT broker
     client.publish(pub_topic, jsonBuffer);
     Serial.println("Data sent to MQTT broker");
   }
 }


 client.loop();
 delay(100);
}
