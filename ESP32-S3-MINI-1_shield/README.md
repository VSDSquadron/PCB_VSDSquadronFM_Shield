![Screenshot (692)](https://github.com/user-attachments/assets/79eb0846-71fb-40d5-9943-f3b465bc3e13)![Screenshot (684)](https://github.com/user-attachments/assets/c689b0a2-a5b3-4608-be09-0d71d03188f7)# VSD Squadron FM ESP32-S3-MINI-1 Shield

This repository contains the design files and instructions for creating a production-level PCB shield that connects the ESP32-PICO-D4 with the VSDSquadron FPGA Mini. This documentation outlines the design process, connections, and resources used.

## Table of Contents

- [Introduction](#introduction)
- [Theory](#theory)
- [Design Procedure](#design-procedure)
- [Connections Overview](#connections-overview)
- [Design Rules Check](#design-rules-check)
- [Warnings and Considerations](#warnings-and-considerations)
- [BOM and Parts Management](#bom-and-parts-management)
- [Resources](#resources)

## Introduction

The goal of this project is to design a PCB shield that facilitates communication between the ESP32-PICO-D4 and the VSDSquadron FPGA Mini. This document provides an overview of the design process, pin connections, and additional considerations for production.

## Theory Content

### Introduction to the Shield

The ESP32-PICO-D4 is a powerful microcontroller with integrated Wi-Fi and Bluetooth capabilities. When combined with the VSDSquadron FPGA Mini, this shield enables advanced functionalities such as:

- **Wireless Communication**: Utilizing the ESP32's Wi-Fi and Bluetooth features.
- **Real-Time Processing**: Leveraging the FPGA's parallel processing capabilities.
- **Flexible I/O Expansion**: Providing additional GPIOs for sensors and actuators.

### Key Concepts

1. **UART Communication**:
   - The shield uses TXD0 and RXD0 pins for serial communication between the ESP32 and the FPGA. This allows for data exchange and command control.

2. **GPIO Management**:
   - Additional GPIOs are available on the ESP32 for connecting various peripherals, enhancing the system's versatility.

3. **Power Management**:
   - The shield includes a 3.3V power supply regulated by an AMS1117, ensuring stable voltage levels for both the ESP32 and FPGA.

4. **Design Considerations**:
   - A design rules check (DRC) was performed to ensure manufacturability based on industry standards.
   - Keepout areas were adjusted to optimize layout without affecting functionality.

[ESP32-S3-MINI-1 Documentation](https://www.espressif.com/documentation/esp32-s3-mini-1_mini-1u_datasheet_en.pdf)

## Use Case Scenarios

### 1. IoT Sensor Network

In an IoT sensor network application, the ESP32 can collect data from various sensors (temperature, humidity, etc.) connected via GPIOs. The data can be processed in real-time by the FPGA and transmitted wirelessly to a cloud server for monitoring.

### 2. Remote Control System

This shield can be used in remote control systems where commands are sent from a mobile app via Bluetooth to control devices connected to the FPGA. The ESP32 handles Bluetooth communication while the FPGA executes control logic.

### 3. Robotics Control

In robotics applications, this setup can manage multiple actuators and sensors. The ESP32 can communicate with a smartphone or computer interface to receive commands, while the FPGA processes sensor data to make real-time decisions.

### 4. Data Logger

The combination of ESP32 and FPGA can be employed as a data logger for various environmental parameters. The ESP32 collects data from sensors and stores it locally or transmits it to a remote server for analysis.

## Design Procedure

1. **Schematic Creation**: 
   - The schematic was created using KiCad 8.0.8, ensuring all components were correctly placed and connected.
  a) Open KiCad and go to create new project.
  ![Screenshot (671)](https://github.com/user-attachments/assets/7670cab4-b8e4-48a9-b267-8c78d2960c0a)
  b) Select your desired save path and name.
  ![Screenshot (672)](https://github.com/user-attachments/assets/9241d784-c861-40a9-ac61-b2bc8c82b63e)
  c) First download the VSDSquadron FM library, paste and (if zip extract it) it inside your project folder.
  ![Screenshot (674)](https://github.com/user-attachments/assets/ab7758c8-2f19-400b-9b91-491e671341d6)
  d) Go to preferences and select manage symbol library to add the VSDSquadron FM Shield Symbol, select specific project option and choose the `.sym` file `\library\symbols`.
  ![Screenshot (673)](https://github.com/user-attachments/assets/d3e33727-a646-4b65-8f19-2ee0e423040f)
  ![Screenshot (676)](https://github.com/user-attachments/assets/d274d48b-7005-420d-a05a-0813c229e085)
  ![Screenshot (677)](https://github.com/user-attachments/assets/85fbc455-25db-4351-ac10-2e1af3906705)
  ![Screenshot (678)](https://github.com/user-attachments/assets/233a4a62-6427-4018-8328-4a9b6a5a224c)
  e) Similarly add the footprint by choosing the `.pretty` folder.
  ![Screenshot (679)](https://github.com/user-attachments/assets/08ee916d-d3d7-477f-abe5-15f0f305666b)
  ![Screenshot (680)](https://github.com/user-attachments/assets/67d87d12-bd40-4f01-9795-79eeb12ecf33)
  f) Open the schematic file in side tab and you can start creating your schematic.
  ![Screenshot (681)](https://github.com/user-attachments/assets/16baf4af-1410-410d-a4f0-c7dbb50426ba)

## Pin Connections Table

| **ESP32-PICO-D4 Pin** | **Function**              | **Suggested Connection on VSDSquadron FPGA Mini** |
|------------------------|---------------------------|--------------------------------------------------|
| IO0                   | GPIO / Input              | Any available GPIO pin (avoid power pins)        |
| IO1                   | UART TX                  | Connect to a UART RX pin on FPGA                 |
| IO3                   | UART RX                  | Connect to a UART TX pin on FPGA                 |
| IO4                   | GPIO / Input              | Any available GPIO pin                           |
| IO11                  | GPIO / Output             | Any available GPIO pin                           |
| IO12                  | GPIO / Output             | Any available GPIO pin                           |
| IO13                  | GPIO / Output             | Any available GPIO pin                           |
| IO14                  | GPIO / Output             | Any available GPIO pin                           |
| IO15                  | GPIO / Output             | Any available GPIO pin                           |
| IO16                  | GPIO / Output             | Any available GPIO pin                           |
| IO45                  | GPIO                      | Any available GPIO pin                           |
| IO46                  | GPIO                      | Any available GPIO pin                           |
| USB_D-                | USB Data Negative         | Any available GPIO pin                           |
| USB_D+                | USB Data Positive         | Any available GPIO pin                           |
| TXD0                  | UART TX                  | Any available GPIO pin                           |
| RXD0                  | UART RX                  | Any available GPIO pin                           |
| GND                   | Ground                   | Connect to GND on FPGA                           |
| 3V3                   | Power Supply (3.3V)      | Connect to 3.3V power input on FPGA              |

---

## Additional Components to Consider

When designing the shield, here are some extra components you might find useful:

| **Component**       | **Description**                                                                 |
|----------------------|-------------------------------------------------------------------------------|
| AMS1117             | 3.3V Low Dropout Regulator (LDO) for stable power supply. Ensure it can handle the current requirements of both the ESP32 and FPGA. |
| Decoupling Capacitors| Place capacitors (e.g., 100nF) close to the power pins of both ESP32 and FPGA for noise reduction. |
| Pull-Up Resistors    | Use for any input pins that require stable HIGH states. Common values are 4.7kΩ or 10kΩ. |
| LED Indicators       | For debugging purposes, you can add LEDs connected to IO12 pin to indicate status or activity. |

---

## Pull-Up Resistors

Pull-up resistors are typically used with input pins to ensure they are in a defined state when not actively driven. For the ESP32-PICO-D4, consider using pull-up resistors on the following pins:

| **Pin**  | **Function**             | **Recommended Resistor Value** |
|----------|--------------------------|---------------------------------|
| IO0      | Boot Mode Selection      | 10kΩ                         |
| IO2      | Boot Mode Selection      | 10kΩ                         |
| EN       | Enable Pin               | 10kΩ                         |

---

## Schematic Creation Steps

### Step 1: Define Component Placement
1. **Identify the ESP32-S3-MINI-1 module:**
   - Locate the ESP32 module in your schematic.
   - Ensure pin orientation matches your design.

2. **Locate supporting components:**
   - Place external capacitors (decoupling and filtering) close to the ESP32 power pins.
   - Add a crystal oscillator (if not integrated).
  ![image](https://github.com/user-attachments/assets/c279bd6f-3ede-4f4e-beb0-c58b9099cf37)

### Step 2: Power Supply Design
- **Connect the 3.3V pin to a regulated power supply.**
- Include decoupling capacitors (e.g., 0.1µF and 10µF) near the ESP32 power input for noise suppression.
- Connect the ground pin (GND) to the common ground plane.

### Step 3: Interface Connections
- **UART Pins (IO1, IO3):** Connect TXD and RXD to debug UART headers for serial communication.
- **GPIO Pins (e.g., IO4, IO11):** Reserve these for user-defined I/O operations or sensors.

### Step 4: Add Headers and Connectors
- Add pin headers for easy interfacing with the VSDSquadron FPGA Mini.
- Include connectors for external devices or modules (e.g., I2C or SPI sensors).
Also add you can edit the page settings by clicking on the right lower box as
   ![Screenshot (683)](https://github.com/user-attachments/assets/ac155b97-bd88-4c57-873f-e9cc55c4b232)

### Step 5: Routing and Ground Planes
- Carefully route traces to minimize noise and interference.
- Use a solid ground plane to reduce electromagnetic interference (EMI).
  ![Screenshot (682)](https://github.com/user-attachments/assets/949f8825-5b6a-4bd1-86b9-5077818cf76a)
Note : Above image contain slight few changes in future

### Step 6: Assign Footprints
- Open the assign footprint option in the toolbar and assign necessary footprints associated to the components you have to selected to use.
  ![Screenshot (771)](https://github.com/user-attachments/assets/f3d2a9c9-6fbb-428a-b1f3-9c7a68031e1c)
Note: Above image corresponds to the upadated schematic
  ![Screenshot (772)](https://github.com/user-attachments/assets/ece24706-6f7c-4e20-bcae-df135bcc8b3e)

### Step 7: Final Review and Testing
- Verify all connections against the schematic.
- Perform design rule checks (DRC) in your PCB software, by running Run Check
- Test the prototype for correct functionality.
  ![Screenshot (684)](https://github.com/user-attachments/assets/e41e2f4c-5447-4b54-b0b5-77b83964b144)
  ![Screenshot (685)](https://github.com/user-attachments/assets/fd461cd3-0897-4add-a50e-fff16b1c37f4)
  ![Screenshot (686)](https://github.com/user-attachments/assets/f7197f0c-2c74-4509-9c76-91c7e91a1353)

---

## Notes
- Ensure all components are rated for the operating voltage and current.
- Properly label all pins and connectors for ease of debugging and testing.

2. **PCB Layout**: 
   - After finalizing the schematic, the PCB layout was designed considering optimal component placement and routing.
   
  a) After zero errors by DRC check go back to home page of KiCad and choose PCB editor option.
  ![Screenshot (687)](https://github.com/user-attachments/assets/f9b83712-6164-434c-abf3-e2aa38aec83f)
  b) Ensure that you have installed the following plugins.
  ![Screenshot (742)](https://github.com/user-attachments/assets/6ef817d3-d00a-4653-88e4-df536e5a58a0)
## PCB Creation Steps

### Step 1: Defining Board Setup
1. **Open Board Setup**
   - Locate the board setup option in file dropdown in toolbar.
   - Click on the board setup and new window will pop-up.
   
2. **Set Board Editor Layers**
    - Tick on the desired layers as
    ![Screenshot (689)](https://github.com/user-attachments/assets/9d94e240-e30a-4e3c-9618-57203d4e7998)

3. **Set PCB Physical Design**
    - Open the `Physical Stackup` option in the dropdown.
    - Set the layers as desired
      ![Screenshot (690)](https://github.com/user-attachments/assets/4a2e0c9a-baa1-4162-b5f3-88995aee3025)
      
4. **Define constraints**
    - Open the `Constraints` option in the dropdown.
    - Keeping the minimum design rule values of ESP32 set the constraint values
      ![Screenshot (691)](https://github.com/user-attachments/assets/ca5216cc-4a5e-488e-8fef-5cf9584662fe)
      
5. **Define the pre-defined sizes**
    - Open the `pre-defined sizes` section in the dropdown.
    - Introduce your sizes (Here i am refering to the [Lion Circuits Capabilities]([https://www.lioncircuits.com](https://www.lioncircuits.com/pcb-manufacturing-capabilities))
      ![Screenshot (692)](https://github.com/user-attachments/assets/5948abb5-b49f-4f11-bbec-3c4f07fd8de2)
### Step 2: Create PCB from Schematic
   - Open the PCB Editor
     ![Screenshot (693)](https://github.com/user-attachments/assets/30273d5c-6d17-4845-bc43-5eb22c11ef3a)
   - Go to `Update PCB from Schematic` in the tool bar and run it.
     ![Screenshot (694)](https://github.com/user-attachments/assets/7bdb3bf4-6e97-4c8f-9058-385393998df7)
     ![Screenshot (695)](https://github.com/user-attachments/assets/d24b9592-fde3-407e-b109-f8b91ae4d8c0)

4. **Design Rules Check**: 
   - A thorough design rules check (DRC) was performed using guidelines from Lion Circuits capabilities to ensure manufacturability.

## Connections Overview

Below is a table outlining the connections between the ESP32-PICO-D4 and VSDSquadron FPGA Mini:

| **ESP32-PICO-D4 Pin** | **Function**                | **Connection on VSDSquadron FPGA Mini** |
|------------------------|-----------------------------|-----------------------------------------|
| TXD0 (GPIO1)          | UART Transmit               | Connect to UART RX pin                  |
| RXD0 (GPIO3)          | UART Receive                | Connect to UART TX pin                  |
| IO0                    | GPIO / Input                | Any available GPIO pin                  |
| IO2                    | Boot Mode Selection         | Pull-up resistor recommended             |
| GND                    | Ground                      | Connect to GND                          |
| 3V3                    | Power Supply (3.3V)        | Connect to 3.3V power input             |

## Design Rules Check

The design rules check was conducted based on guidelines from [Lion Circuits Capabilities](https://www.lioncircuits.com). This ensures that the PCB meets industry standards for manufacturability and reliability.

## Warnings and Considerations

During the design process, a warning was generated due to the deletion of the keepout area around the ESP32-Mini. This warning can be safely ignored as it does not affect the functionality or manufacturability of the PCB.

## BOM and Parts Management

The JLPCB plugin was utilized to produce the PCB layout efficiently. Additionally, all LSCS part numbers were saved to a `bom.csv` file for easy reference during assembly.

## Conclusion

The ESP32-PICO-D4 shield for VSDSquadron FPGA Mini opens up numerous possibilities in embedded systems design, offering flexibility in communication, processing power, and peripheral management. This document serves as a theoretical foundation and practical guide for implementing this technology in various applications.

## Resources
- [ESP32-S3-MINI-1 Documentation](https://www.espressif.com/documentation/esp32-s3-mini-1_mini-1u_datasheet_en.pdf)
- [KiCad Documentation](https://www.kicad.org/documentation/)
- [Lion Circuits Capabilities](https://www.lioncircuits.com)
- [JLPCB Plugin for KiCad](https://github.com/jlpcb/jlpcb-kicad-plugin)

For any questions or contributions, feel free to open an issue or submit a pull request!




Author: Aaryan Sharma
