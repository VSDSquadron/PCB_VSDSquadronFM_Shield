# VSDSquadron FM Keyboard PCB LEDs Shield

# Mechanical Keyboard PCB using LEDs and VSDSquadron FM ( LED Interfacing )

This project focuses on designing a shield using VSDSquadron FM library. The shield is **Mechanical Keyboard PCB** which is made using **KiCad EDA 8.0.7** for schematic design and PCB layout. The PCB integrates LEDs for dynamic lighting and utilizes the **VSDSquadron FM** framework for firmware, making it a versatile and visually appealing solution for custom keyboard enthusiasts.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Tools Used](#tools-used)
3. [Installation](#installation)
4. [Schematic Design](#schematic-design)
5. [PCB Layout](#pcb-layout)
6. [ERC and DRC Checks](#erc-and-drc-checks)
7. [3D Viewer](#3d-viewer)
8. [Bill of Materials (BOM)](#bill-of-materials-bom)
9. [Applications](#applications)
10. [References](#references)
11. [License](#license) 
12. [Author](#author)
    
---

## 1. Project Overview

- **Purpose**: To design a custom PCB for a mechanical keyboard with LED lighting and advanced firmware support.
  Built using KiCad 8.0, this PCB features a matrix keyboard design with support for customizable RGB lighting and versatile firmware, enabling advanced functionality and user-defined key mappings.

- **Key components include**:

- LED integration for visual effects, enhancing aesthetics and user feedback.
- Matrix scanning technology for efficient key detection.
- Expandable design for use in gaming, productivity, or assistive devices.

The project covers a complete PCB development workflow, including schematic creation, footprint assignment, layout design, electrical rule checks (ERC), design rule checks (DRC), 3D visualization, and generating a bill of materials (BOM). It is ideal for educators, and professionals seeking to create high-performance, customizable keyboards for various applications.

---

## 2. Tools Used

- **KiCad EDA 8.0.7**: For schematic capture, PCB layout, and 3D rendering.
- **VSDSquadron FM**: For firmware development.
- **JLC PCB Fabrication Toolkit**: Additional software for BOM generation and assembly.
- **Kibuzzard**: Additional Library from Plugin and Content Manager.
  
---

## 3. Installation

1. **Install KiCad EDA 8.0.7**:  
   Download and install from the official [KiCad website](https://www.kicad.org).

   Open the project:
   Load the .kicad_pro file in KiCad to access the schematic and PCB design files.

---

## 4. Schematic Design
The schematic outlines the matrix design for key switches, LED drivers, and VSDSquadron FM connections.

Key Features:
* Matrix configuration for keyboard rows and columns.
* Integrated LED drivers for lighting control.
* Connection to the VSDSquadron FM framework.

---

## 5. PCB Layout
The PCB layout ensures optimal routing and signal integrity while accommodating all components.

Front Copper Layer:

Back Copper Layer:

Key Features:
* Carefully routed traces for LED control.
* Footprints for standard MX-style mechanical switches.
* Compact design with minimal interference.

## 6. ERC and DRC Checks
- ERC (Electrical Rule Check): Verified for schematic consistency and correct pin configurations.
- DRC (Design Rule Check): Passed for trace clearances, via sizes, and other manufacturing constraints.

## 7. 3D Viewer
- The 3D viewer in KiCad provides a realistic preview of the PCB, showing component placement and board dimensions.
- Use the 3D Viewer feature in KiCad to visualize your design before manufacturing.

## 8. Bill of Materials (BOM)
A detailed BOM is included, listing all components:

- Mechanical Switches: Compatible with MX-style switches.
- LEDs: WS2812B addressable LEDs.
- Download the BOM file: bom.csv (https://github.com/Githubforbilwa/VSDSquadron_FM_Shield/blob/main/Keyboard_PCB_LEDs_Shield/production/bom.csv).

## 9. Applications
* Applications of the Mechanical Keyboard PCB Using LEDs and VSDSquadron FM
1. Custom Mechanical Keyboards

- Perfect for mechanical keyboard enthusiasts looking to build personalized keyboards with customizable layouts and lighting effects.
- Allows users to experiment with unique key arrangements, switch types, and features.
  
2. Gaming Keyboards

- With support for addressable LEDs, this PCB can be used to create high-performance gaming keyboards with vibrant RGB lighting effects synchronized to gameplay.
- Provides low-latency response and macro programming for competitive gaming.

3. Educational Tool

 A great learning platform for electronics students and hobbyists to understand:
- PCB design and manufacturing.
- Matrix scanning in keyboards.
- Firmware development using VSDSquadron FM.
- Encourages exploration of embedded systems and hardware programming.
  
4. Prototyping for Manufacturers

- Can be used by keyboard manufacturers to prototype new designs or test features such as dynamic lighting or alternative layouts before mass production.
  
5. IoT and Smart Device Integration

- The PCB can be adapted to serve as an input interface for smart home devices or IoT systems.
- Useful for creating smart keyboards that connect to various devices via Bluetooth, Wi-Fi, or USB.

6. Assistive Technology Devices

- Customizable layouts and programmable firmware make it suitable for assistive devices tailored for individuals with disabilities.

7. Interactive Art Installations

- The RGB LED integration enables the PCB to be used in art installations requiring interactive lighting effects triggered by key presses.

8. Workstation Productivity Tools

- Custom PCBs can enable keyboards designed for professional workflows (e.g., CAD, video editing, programming), with macro keys and lighting for task-specific functions.

9. Hobby Projects

- Suitable for DIY projects or hobbyists exploring keyboard customization, firmware development, and soldering.

10. Retro Keyboard Recreation

- Recreate retro-style keyboards with modern functionality while maintaining classic aesthetics, enhanced by programmable lighting.

11. Portable Keyboards for Mobile Devices

- Design compact, portable keyboards for smartphones, tablets, or laptops, leveraging low-power designs and ergonomic layouts.

12. Open-Source Hardware Development
    
- Encourage the open-source hardware community to build upon the design by contributing new layouts, firmware features, or modular add-ons.

13. Teaching STEM Concepts
    
- Use the project as a hands-on STEM education resource to teach principles of electronics, circuit design, software programming, and human-computer interaction.

14. Creative Studio Tools
    
- Develop keyboards optimized for creative professionals, such as video editors, or graphic designers, with configurable shortcuts and interactive lighting for inspiration.

15. Ergonomic Keyboard Prototypes
    
- Enable the creation of ergonomic keyboard layouts optimized for comfort and reduced strain during long hours of typing.

---

## 10. References 
- https://github.com/ebastler/marbastlib

- Referred keyboard layout for the complete design:

![Referred_keyboard_layout](https://github.com/user-attachments/assets/9ab065c1-98ef-491e-b0b7-72acb6d3723a)


---

## 11. License
This project is licensed under the MIT License.

---

## 12. Author 
- Bilwa Ghisad

- Email: bilwaghisad@gmail.com
- GitHub: Githubforbilwa




