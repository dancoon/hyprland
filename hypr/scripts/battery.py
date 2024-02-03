#!/usr/bin/env python
import subprocess
import time

def check_battery():
    while True:
        battery_status = subprocess.check_output(["cat", "/sys/class/power_supply/BAT0/status"]).decode().strip()
        battery_percentage = int(subprocess.check_output(["cat", "/sys/class/power_supply/BAT0/capacity"]).decode().strip())

        if battery_status == "Discharging" and battery_percentage <= 20:
            subprocess.run(["dunstify", "-u", "CRITICAL", "Battery Low", f"Battery is at {battery_percentage}%. Connect the charger."])

        if battery_status == "Charging" and battery_percentage >= 80:
            subprocess.run(["dunstify", "-u", "NORMAL", "Battery Charged", f"Battery is at {battery_percentage}%. You can unplug the charger."])

        time.sleep(300)  # Sleep for 5 minutes before checking again

check_battery()
