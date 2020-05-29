#!/usr/bin/env python3

# IMPORT
import sys
import time
import board
import adafruit_dht

# ARGUMENTS
# 0 = Script
# 1 = Board Port (Expects a Digital Port. Example: "D5")
# 2 = Component Variation (Expects "DHT11" or "DHT22")
# 3 = Temperature Variale ID (Expects Forest Platform VID)
# 4 = Cycle (Expects cycle expressed in minutes)

# ARGUMENTS: Definitions
print (f"SCRIPT (filename) = {sys.argv[0]}")
print (f"CONNECTION (port) = {sys.argv[1]}")
print (f"COMPONENT (variation) = {sys.argv[2]}")
print (f"TEMPERATURE (vid) = {sys.argv[3]}")
print (f"HUMIDITY (vid) = {sys.argv[4]}")

# BOARD & Component
#
# TODO: ARGUMENTS
#
device = adafruit_dht.DHT22(board.D5)
#
#device_str = f"device = adafruit_dht.{sys.argv[2]}(board.{sys.argv[1]})"
#exec(device_str)
#print("DEVICE STR =", device_str)
#device = exec(device_str)

# Time (UNIX MS)
t = time.time()
print (f"TIME (unix ms) = {t}")

# BOARD: Values
temp_value = device.temperature
print (f"TEMPERATURE (°C) = {temp_value}")
humi_value = device.humidity
print (f"HUMIDITY (%RH) = {humi_value}")

# LOG: Variables
filename = time.strftime("%Y-%m") # Time Prefix

# LOG: Fix, Temperature (VID)
temp_path = f"/var/log/dasos/sense/{sys.argv[3]}/{filename}.csv" # SP = Sense Path
humi_path = f"/var/log/dasos/sense/{sys.argv[4]}/{filename}.csv" # SP = Sense Path
print ("TEMP LOG PATH =", temp_path)
print ("HUMI LOG PATH =", humi_path)

# RECORD: Temperature CSV
temp_csv = f"{t},{temp_value}"
print("TEMP RECORD (csv) =", temp_csv)

# RECORD: Humidity CSV
humi_csv = f"{t},{humi_value}"
print("HUMI RECORD (csv) =", humi_csv)

# SENSE: Write Temperature CSV Record
with open(temp_path, "a") as log:
    log.write("\n")
    log.write(temp_csv)
    log.close()

# SENSE: Write Humidity CSV Record
with open(humi_path, "a") as log:
    log.write("\n")
    log.write(humi_csv)
    log.close()

# SENSE: Ready
print("SENSE Record Generated")
