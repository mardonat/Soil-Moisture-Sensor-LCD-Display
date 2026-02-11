# Soil-Moisture-Sensor-LCD-Display

## Introduction
A simple setup was constructed for easy calibration of TDR soil moisture sensors, allowing moisture values from individual sensors to be read directly from the display.
After successful calibration, the sensors will be installed in the field and integrated into the Citizen Science project as part of the “Klimawerkstatt Fläming - Gemeinsam grüner leben” (Fläming Climate Workshop - Living Greener Together) project in the water map https://wasserkarte.badbelzig-klimadaten.de/.

## Description
The program and setup were designed for the Soil Moisture Sensor (SN 300SD TR N01). These are inexpensive sensors that indirectly determine the water content using the TDR measurement principle. The raw signals are output in V% through an unknown internal conversion and parameters.All parts needet for that setup are listed in Fig.1.


<img src="https://github.com/mardonat/Soil-Moisture-Sensor-LCD-Display/blob/main/images/parts.png" width="700" />  

Fig.1: All parts needed for this project.
<br/>
<br/>


All cables from the individual sensors were connected in a junction box using Wago clamps (Fig.2). Communication with the sensors takes place via Modbus protocol. Modbus RTU sensors communicate using a master-slave architecture over RS-485, requiring each sensor to have a unique address to be identified on a shared cable.
<br/>
<br/>


<img src="https://github.com/mardonat/Soil-Moisture-Sensor-LCD-Display/blob/main/images/connections.png" width="700" />  

Fig.2: Schematic drawing and wiring of the 4 sensors in the junction box
<br/>
<br/>
<br/>
The wiring is as shown in Fig. 3. I used jumper cables and a breadboard for the setup.
<br/>
<br/>
<img src="https://github.com/mardonat/Soil-Moisture-Sensor-LCD-Display/blob/main/images/layout.png" width="700" />

Fig.3: Layout of connections between Pico, MAX485 interface module and sensors
<br/>
<br/>
<br/>
The Pico is operated with micropython. The main.py file was copied to the Pico via mpremote. The finished circuit and the output on the LCD display can be seen in Fig. 4.
<br/>
<br/>
<img src="https://github.com/mardonat/Soil-Moisture-Sensor-LCD-Display/blob/main/images/readings.png" width="700" />

Fig.4: Final setup and simultaneous display of sensor values, which are updated every few seconds.
<br/>
<br/>
<br/>



