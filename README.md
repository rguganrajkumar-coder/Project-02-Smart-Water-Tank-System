# SMART WATER TANK LEVEL MONITORING AND USAGE SYSTEM

## Project Overview

The **Smart Water Tank Level Monitoring and Usage System** is a Python-based project designed to monitor water levels, manage water usage, and control motor operations based on the tank's water level.

The project provides a console-based Python application and a separate web dashboard to demonstrate water level monitoring and management.

## Features

- Water level monitoring
- Automatic motor ON/OFF control based on water level
- Water usage management
- Tank filling management
- Water usage history
- Tank filling history
- Water level alerts
- Interactive console menu
- Web-based monitoring dashboard

## Water Level and Motor Control

The system uses the following conditions to control the motor:

| Water Level | Motor Status |
|---|---|
| 0% – 30% | ON |
| 31% – 89% | Maintains previous status |
| 90% – 100% | OFF |

### Water Level Alert System

| Water Level | Alert |
|---|---|
| 0% – 5% | Critical |
| 6% – 15% | Very Low |
| 16% – 30% | Low |
| 31% – 60% | Normal |
| 61% – 85% | High |
| 86% – 99% | Very High |
| 100% | Tank Full |

## Technologies Used

### Python Application
- Python
- Random
- Time
- Datetime

### Web Dashboard
- HTML5
- CSS3
- JavaScript

### Development Tools
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
smart-water-tank-system/
│
├── smart_water_tank.py
├── index.html
└── README.md
```

## How the System Works

1. The application starts with an initial simulated water level.
2. The current water level is displayed.
3. The motor status is controlled according to the water level.
4. Users can consume water from the tank.
5. Users can fill the tank when the motor is ON.
6. The application records water usage and filling history.
7. Alerts are displayed according to the current water level.
8. Users can view the usage and filling history through the menu.

## Installation and Execution

### Step 1: Clone the Repository

```bash
git clone https://github.com/rguganrajkumar-coder/smart-water-tank-system.git
```

### Step 2: Open the Project Folder

```bash
cd smart-water-tank-system
```

### Step 3: Run the Python Application

```bash
python smart_water_tank.py
```

### Step 4: Open the Web Dashboard

Open the `index.html` file in your web browser.

## Console Application Menu

The Python application provides the following options:

```text
1. Use Water
2. Fill Tank
3. View Usage History
4. View Fill History
5. Exit
```

## Important Note

- The initial water level is simulated using Python's random module.
- The Python application does not currently use physical sensors or hardware.
- Water usage is tracked using changes in the tank's percentage level.
- The web dashboard operates independently and does not receive live data from the Python application.

## Future Enhancements

- Integration with ESP32 or Arduino.
- Real-time water level monitoring using ultrasonic sensors.
- IoT-based remote monitoring.
- Mobile application integration.
- Cloud-based data storage.
- Water consumption analytics.
- Notifications for low and full water levels.

## Developer

**Guganraj R**

B.E. Computer Science and Engineering  
K. Ramakrishnan College of Engineering (KRCE)  
Tiruchirappalli, Tamil Nadu, India

- GitHub: https://github.com/rguganrajkumar-coder
- Portfolio: https://rguganrajkumar-coder.github.io/guganraj-portfolio/

---

**SMART WATER TANK LEVEL MONITORING AND USAGE SYSTEM**

*Monitoring Water. Managing Usage. Saving Resources.*
