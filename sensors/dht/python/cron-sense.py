#!/usr/bin/env python3

# IMPORT
import sys
import time
import board
import adafruit_dht

# ARGUMENTS
# 0 = Script
# 1 = Board Pin (Expects a Digital Port. Example: "D5")
# 2 = Component Variation (Expects "DHT11" or "DHT22")
# 3 = Temperature Variale ID (Expects Forest Platform VID)
# 4 = Cycle (Expects cycle expressed in minutes)

# ARGUMENTS: Definitions
script = sys.argv[0]
print ("SCRIPT =",script)
board_pin = sys.argv[1]
print ("Board Connection =",board_pin)
board_component = sys.argv[2]
print ("Board Component =",board_component)
temp_vid = sys.argv[3]
print ("Temperature VID =",temp_vid)
humi_vid = sys.argv[4]
print ("Humidity VID =",humi_vid)

# BOARD & Component
#
# TODO: ARGUMENTS
#
device = adafruit_dht.DHT22(board.D5)

# Time (UNIX MS)
t = time.time()
print("Time =", t)

# BOARD: Values
temp_value = device.temperature
humi_value = device.humidity
print("Temperature =", temp_value, "°C")
print("Humidity =", humi_value, "%RH")

# LOG: Fix, Global
pre = time.strftime("%Y-%m-")
file = "cron-sense.csv"

# LOG: Fix, Temperature (VID)
temp_vid = sys.argv[3]
temp_path = "/var/log/dasos/sense/" + temp_vid + "/" + pre + file
print ("Temperature Log Path =", temp_path)

# LOG: Fix, Humidity (VID)
humi_vid = sys.argv[4]
humi_path = "/var/log/dasos/sense/" + humi_vid + "/" + pre + file
print ("Humidity Log Path =", humi_path)

# RECORD: Temperature CSV
temp_csv = f"{t},{temp_value}"
print("Temperature Record =", temp_csv)

# RECORD: Humidity CSV
humi_csv = f"{t},{humi_value}"
print("Humidity Record =", humi_csv)

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
