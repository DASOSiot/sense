#!/usr/bin/env python3

# IMPORT
import sys
import time
import board
import adafruit_dht

# ARGUMENTS
#print(f"Name of the script      : {sys.argv[0]=}")
#print(f"Arguments of the script : {sys.argv[1:]=}")

# BOARD >> TODO: Arguments (Model + Port)
dhtDevice = adafruit_dht.DHT22(board.D5)

# Time (UNIX MS)
t = time.time()
print("Time =", t)
# Values from Device
v_temp = dhtDevice.temperature # Print the values to the serial port
v_humi = dhtDevice.humidity # Print the values to the serial port
print("Temperature =", v_temp, "°C")
print("Value =", v_humi, "%RH")

# RECORD: Temperature CSV
csv_temp = f"{t},{v_temp}" # String Composition
print("Temperature Record =", csv_temp)

# SENSE: Write Temperature CSV Record
# TODO: Replace "vid-000" with argument VID
with open("/var/log/dasos/sense/vid-000/cron-sense.csv", "a") as log: # Open the file in append ('a')
    log.write("\n") # Append Line
    log.write(csv_temp) # Append Record
    log.close() # LOG: Close

# RECORD: Humidity CSV
csv_humi = f"{t},{v_humi}" # String Composition
print("Humidity Record =", csv_humi)

# SENSE: Write Humidity CSV Record
#
# TODO: Replace "vid-001" with argument VID
#
with open("/var/log/dasos/sense/vid-001/cron-sense.csv", "a") as log: # Open the file in append ('a')
    log.write("\n") # Append Line
    log.write(csv_humi) # Append Record
    log.close() # LOG: Close

# SENSE: Ready
print("SENSE Record Generated")
