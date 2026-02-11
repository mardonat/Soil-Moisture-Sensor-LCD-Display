# Soil-Moisture-Sensor-LCD-Display

## Introduction
A simple setup was constructed for easy calibration of TDR soil moisture sensors, allowing moisture values from individual sensors to be read directly from the display.
After successful calibration, the sensors will be installed in the field and integrated into the Citizen Science project as part of the “Klimawerkstatt Fläming - Gemeinsam grüner leben” (Fläming Climate Workshop - Living Greener Together) project in the water map https://wasserkarte.badbelzig-klimadaten.de/.

## Description
The program and setup were designed for the Soil Moisture Sensor (SN 300SD TR N01). These are inexpensive sensors that indirectly determine the water content using the TDR measurement principle. The raw signals are output in V% through an unknown internal conversion and parameters.


<img src="https://github.com/mardonat/Soil-Moisture-Sensor-LCD-Display/blob/main/images/parts.png" width="700" />

Fig.1: All parts needed for this project.

<img src="https://github.com/mardonat/Soil-Moisture-Sensor-LCD-Display/blob/main/images/connections.png" width="700" />

Fig.2: Schematic drawing and wiring of the 4 sensors in the junction box

<img src="https://github.com/mardonat/Soil-Moisture-Sensor-LCD-Display/blob/main/images/layout.png" width="700" />

Fig.3: Layout of connections between Pico, MAX485 interface module and sensors

<img src="https://github.com/mardonat/Soil-Moisture-Sensor-LCD-Display/blob/main/images/readings.png" width="700" />

Fig.4: Final setup and simultaneous display of sensor values, which are updated every few seconds.



