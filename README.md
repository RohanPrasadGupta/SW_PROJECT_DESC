# User stories and acceptance criteria

## Smart Construction Management System

1. As a **construction manager**, I want to  **be informed that how many labours come to the construction site** so that **I can calculate and estimate the number of labours on the construction site.**
   * Scenario: **attendance of labours**, given **actual labours on the construction site**, when **the labours entering to the construction site**, then **verify the location and current status during working hours.**

2. As a **construction manager**, in order to **determine the amount of overtime**, I need to **see the laborers' overtime hours**.
   * Scenario: **labour after working hours**, **given number of labours**, when **stay working on construction site**.

3. As a **construction manager**, I want to **be informed of an emergency labour situation** so that I can **notify to the emergency team**.
   * Scenario: **Emergency aid needed**, given **Wifi Connection**, when **Emergency needed from injured labour**, then **necessary data of injured labour will send to the construction supervisor with Wifi Connection to call emergency team**.
   
4. As a **labour**, I want to **notify the emergency alert** so that **I can get the emergency respond**.
   * Scenario: **The labour is injured**, given **Wifi connection**, when **injury happenes**, then **I will press the injured alert button.**
   * Scenario: **Fire Case**, given **Wifi connection**, when **Fire burning occurs**, then **I will press the fire alert button.**

# Software Architecture and Behaviors

## System Design
![System structure](https://user-images.githubusercontent.com/126549879/229776705-c9ef0782-cb6a-4383-a62f-763a10d5fffd.jpeg)

## System Overview
![image](https://user-images.githubusercontent.com/54372454/223699373-3dee8015-4997-4d34-836a-5a04be1c72cf.png)

## Case Structure

## For Case to Calculate the working Hour
![image](https://user-images.githubusercontent.com/54372454/223031744-be9eeb63-3362-4472-a5be-aff21e1f46e5.png)

## For Case to Alert the Emergency Unit
![image](https://user-images.githubusercontent.com/54372454/223030034-9302109a-0127-4ff2-a6c7-b3f2c7b25b6a.png)

## For Case to Get Emergency Respond
![image](https://user-images.githubusercontent.com/54372454/223699747-8762d85b-d853-4869-ab08-42205329b70b.png)

## Objectives
1.
2.
3.

## Project brief


## Members

1.	Zun Khet Wai (zunkhetwai@gmail.com)
2.	Hay Man Htun (hayman.h@live.ku.th)
3.	ROHAN PRASAD GUPTA (rohanprasadgupta4@gmail.com)
4.	Kyaw Maung Maung Thwin (kyawmgmgthwin12@gmail.com)
5.	Adnan Ali (vu.adnan@gmail.com)

### Hardware
![Picture of group 3 hardware](/images/HW_group_3.jpg)
1. [TTGO T-Beam v1.1](http://www.lilygo.cn/claprod_view.aspx?TypeId=62&Id=1281&FId=t28:62:28) (TTGO T-Beam)
   * [CH9102 USB serial](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102) 
   * GPS NEO-6M <not working>
   * OLED 128x64
   * LoRa 923MHz
2. [TTGO T-Beam](http://www.lilygo.cn/prod_view.aspx?TypeId=50060&Id=1237) (TTGO T-Beam)
   * [CP210x USB serial](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
   * GPS NEO-8M
   * LoRa 923MHz
3. [TTGO T-Beam](http://www.lilygo.cn/prod_view.aspx?TypeId=50060&Id=1237) (TTGO T-Beam)
   * [CP210x USB serial](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
   * GPS NEO
   * LoRa 923MHz
4. [TTGO LORA32 1.6](http://www.lilygo.cn/prod_view.aspx?TypeId=50003&Id=1130&FId=t3:50003:3) (TTGO Lora32-OLED V2.1.6)
   * [CP210x USB serial](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
   * LoRa 923MHz
5. [TTGO LORA32](http://www.lilygo.cn/prod_view.aspx?TypeId=50060&Id=1326&FId=t3:50060:3) (TTGO Lora32-OLED V1)
   * [CP210x USB serial](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
   * LoRa 923MHz
6. [TTGO LORA32](http://www.lilygo.cn/prod_view.aspx?TypeId=50060&Id=1326&FId=t3:50060:3) (TTGO Lora32-OLED V1)
   * [CP210x USB serial](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
   * LoRa 923MHz
