"""
Smart Water Tank System
-----------------------
A console-based water tank monitor with automatic motor control.

Features:
    - Simulated water level sensor
    - Automatic motor ON/OFF control (LOW / HIGH thresholds)
    - Use water and fill tank, with overflow and shortage protection
    - Timestamped usage and fill history
    - Detailed alert levels from critical to full

Run:
    python smart_water_tank.py
"""

import random
import time
from datetime import datetime

# ================= SETTINGS =================

LOW = 30    # motor turns ON at or below this level (%)
HIGH = 90   # motor turns OFF at or above this level (%)

# ================= STATE =================

water_level = 0
motor_on = False
total_usage = 0
usage_history = []   # list of (amount, time) tuples
fill_history = []    # list of (amount, time) tuples


# ================= SENSOR (SIMULATED) =================

def read_sensor():
    """Return a simulated water level reading between 20% and 80%."""
    return random.randint(20, 80)


# ================= HELPERS =================

def current_time():
    """Return the current time as HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")


def ask_amount(prompt):
    """Ask for a whole number greater than 0. Return None if invalid."""
    try:
        value = int(input(prompt))
    except ValueError:
        print("❌ ERROR: Please enter a whole number.")
        return None

    if value <= 0:
        print("❌ ERROR: Amount must be greater than 0.")
        return None
    return value


# ================= HEADER =================

def header():
    """Print the title banner with the current date and time."""
    now = datetime.now()
    print("\n" + "=" * 50)
    print("💧 SMART WATER TANK SYSTEM 💧")
    print("📅 Date:", now.strftime("%d-%m-%Y"))
    print("🕒 Time:", now.strftime("%H:%M:%S"))
    print("=" * 50)


# ================= MODULE 1: MONITORING =================

def monitor():
    """Display and return the current sensor reading."""
    print("\n📡 SENSOR STATUS")
    print(f"Water Level : {water_level}%")
    return water_level


# ================= MODULE 2: MOTOR CONTROL =================

def control(level):
    """Switch the motor on or off based on the water level."""
    global motor_on

    print("\n⚙️ MOTOR CONTROL")
    if level <= LOW:
        motor_on = True
        print("⚠️ Low Level → Motor ON")
    elif level >= HIGH:
        motor_on = False
        print("✅ Tank Full → Motor OFF")
    else:
        print("✔ Level Normal")


# ================= MODULE 3: USER ACTIONS =================

def use_water():
    """Reduce the water level by the amount the user enters."""
    global water_level, total_usage

    used = ask_amount("Enter water used (%): ")
    if used is None:
        return

    if used > water_level:
        print("❌ ERROR: Not enough water in tank!")
        print(f"Available water: {water_level}%")
        print("🚨 ALERT: Usage exceeds available water")
        return

    water_level -= used
    total_usage += used
    now = current_time()
    usage_history.append((used, now))
    print(f"🚿 Used {used}% water at {now}")


def fill_tank():
    """Increase the water level. Only allowed while the motor is ON."""
    global water_level

    if not motor_on:
        print("❌ Motor OFF → Cannot Fill")
        return

    added = ask_amount("Enter water to add (%): ")
    if added is None:
        return

    if water_level + added > 100:
        print("❌ ERROR: Tank will overflow!")
        print(f"Current level: {water_level}%")
        print(f"You can only add up to {100 - water_level}%")
        print("🚨 ALERT: Overflow prevented")
        return

    water_level += added
    now = current_time()
    fill_history.append((added, now))
    print(f"💧 Added {added}% water at {now}")


def show_usage_history():
    """Print every recorded water usage."""
    print("\n📊 USAGE HISTORY")
    if not usage_history:
        print("No usage yet")
        return

    for amount, when in usage_history:
        print(f"Used {amount}% at {when}")


def show_fill_history():
    """Print every recorded tank fill."""
    print("\n💧 FILL HISTORY")
    if not fill_history:
        print("No filling yet")
        return

    for amount, when in fill_history:
        print(f"Added {amount}% at {when}")


def user_action():
    """Show the menu and run the chosen action. Return False to exit."""
    global water_level

    print("\n👤 USER MENU")
    print("1. Use Water")
    print("2. Fill Tank")
    print("3. View Usage History")
    print("4. View Fill History")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        use_water()
    elif choice == "2":
        fill_tank()
    elif choice == "3":
        show_usage_history()
    elif choice == "4":
        show_fill_history()
    elif choice == "5":
        return False
    else:
        print("❌ Invalid Choice")

    # Keep the level within the valid range
    water_level = max(0, min(100, water_level))
    return True


# ================= MODULE 4: DISPLAY =================

def display():
    """Print a summary of the whole system."""
    print("\n📊 SYSTEM STATUS")
    print("-" * 40)
    print(f"Water Level : {water_level}%")
    print(f"Motor       : {'ON' if motor_on else 'OFF'}")
    print(f"Total Usage : {total_usage} units")
    print("-" * 40)


# ================= MODULE 5: ALERT SYSTEM =================

def alert():
    """Print a detailed alert based on the current water level."""
    print("\n🚨 ALERT SYSTEM")

    if water_level <= 5:
        print("🔴 CRITICAL: Tank Almost Empty (0-5%)")
    elif water_level <= 15:
        print("🟠 VERY LOW: Water Level Very Low (6-15%)")
    elif water_level <= 30:
        print("🟡 LOW: Water Level Low (16-30%)")
    elif water_level <= 60:
        print("🟢 NORMAL: Water Level Medium (31-60%)")
    elif water_level <= 85:
        print("🔵 HIGH: Water Level High (61-85%)")
    elif water_level < 100:
        print("🟣 VERY HIGH: Tank Almost Full (86-99%)")
    else:
        print("🔴 FULL: Tank Completely Full (100%)")


# ================= MAIN SYSTEM =================

def show_status():
    """Run one full monitoring cycle."""
    level = monitor()
    control(level)
    display()
    alert()


def main():
    global water_level

    water_level = read_sensor()

    header()
    print("System Started...")
    show_status()

    while True:
        if not user_action():
            print("\n👋 System Stopped")
            break

        header()
        show_status()
        time.sleep(1)


if __name__ == "__main__":
    main()
