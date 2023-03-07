# Userstories and acceptance criteria

## Smart Construction Management System

1. As a **construction manager**, I want to  **be notified that how many labours come to site** so that **I can calculate the number of manpower.**
   * Scenario: **labours attendance**, given **actual labours on site**, when **the labours entering the construction site**, then **check the status and precise location during working hours.**

2. As a **construction manager**, I want to **see the overtime of labours** so that **I can calculate the amount of overtime**.
   * Scenario: **labour after working hours**, **given number of labours**, when **stay working on construction site**, then **check the location and time**.

3. As a **construction manager**, I want to **be notified the emergency case of labour** so that **I can alert to emergency unit**.
   * Scenario: **Emergency aid needed**, given **Wifi Connection**, when **Emergency needed from injured worker**, then **data will send to the supervisor via Wifi Connection to call emergency unit**.
   
4. As a **labour**, I want to **notify the emergency alert** so that **I can get the emergency respond**.
   * Scenario: **The labour is injured**, given **Wifi connection**, when **Injury happenes**, then **I will push the injured alert button.**
   * Scenario: **Fire Case**, given **Wifi connection**, when **Fire burning occurs**, then **I will push the fire alert button.**

# Software Architecture and Behavior

## System Structure

![3067](https://user-images.githubusercontent.com/54372454/223304997-37bba889-5268-46ff-bc82-f2d33435f266.jpg)


## Case Structure
![image](https://user-images.githubusercontent.com/54372454/223024415-06281da4-8bc3-42ad-9a51-14b52dcbe5bf.png)

## For Case to Calculate the working Hour
![image](https://user-images.githubusercontent.com/54372454/223031744-be9eeb63-3362-4472-a5be-aff21e1f46e5.png)

## For Case to Alert the Emergency Unit
![image](https://user-images.githubusercontent.com/54372454/223030034-9302109a-0127-4ff2-a6c7-b3f2c7b25b6a.png)

## For Case to Get Emergency Respond
![image](https://user-images.githubusercontent.com/54372454/223030222-44c6490e-737c-43bd-ab98-fa814c2578c4.png)



## Objectives
1.	.
2.	.
3.	.

## Project brief


## Members

1.	Zun Khet Wai (zunkhetwai@gmail.com)
2.	Kyaw Thiha (kyawthiha7090@gmail.com)
3.	Hay Man Htun (haymanhtun80@gmail.com)
4.	ROHAN PRASAD GUPTA (rohanprasadgupta4@gmail.com)
5.	Kyaw Maung Maung Thwin (kyawmgmgthwin12@gmail.com)
6.	Adnan Ali (vu.adnan@gmail.com)

### Hardware
![Picture of group 3 hardware](/images/HW_group_3.jpg)
1. [TTGO T-Beam v1.1](http://www.lilygo.cn/claprod_view.aspx?TypeId=62&Id=1281&FId=t28:62:28) (TTGO T-Beam)
   * [CH9102 USB serial](https://learn.adafruit.com/how-to-install-drivers-for-wch-usb-to-serial-chips-ch9102f-ch9102) 
   * GPS NEO-6M
   * OLED 128x64
   * LoRa 923MHz
2. [TTGO T-Beam](http://www.lilygo.cn/prod_view.aspx?TypeId=50060&Id=1237) (TTGO T-Beam)
   * [CP210x USB serial](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
   * GPS NEO-8M
   * LoRa 923MHz
3. [TTGO T-Beam](http://www.lilygo.cn/prod_view.aspx?TypeId=50060&Id=1237) (TTGO T-Beam)
   * [CP210x USB serial](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
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
