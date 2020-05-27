#!/usr/bin/env python3

# IMPORT
import sys
import time
import board
import adafruit_dht

# ARGUMENTS
#print(f"Name of the script      : {sys.argv[0]=}")
#print(f"Arguments of the script : {sys.argv[1:]=}")

# BOARD
dhtDevice = adafruit_dht.DHT22(board.D5) # TODO: Arguments (Model + Port)

# Time (UNIX MS)
t = time.time()
print("Time =", t)

# BOARD: Values
v_temp = dhtDevice.temperature
v_humi = dhtDevice.humidity
print("Temperature =", v_temp, "°C")
print("Humidity =", v_humi, "%RH")

# LOG: Fix, Global
pre = time.strftime("%Y-%m-")
file = "cron-sense.csv"

# LOG: Fix, Temperature (VID)
vid_t = "vid-000"
path_t = "/var/log/dasos/sense/" + vid_t + "/" + pre + file
print ("Path =", path_t)

# LOG: Fix, Humidity (VID)
vid_h = "vid-001"
path_h = "/var/log/dasos/sense/" + vid_h + "/" + pre + file
print ("Path =", path_h)

# RECORD: Temperature CSV
csv_temp = f"{t},{v_temp}"
print("Temperature Record =", csv_temp)

# SENSE: Write CSV Record
with open(path_t, "a") as log:
    log.write("\n")
    log.write(csv_temp)
    log.close()

# RECORD: Humidity CSV
csv_humi = f"{t},{v_humi}"
print("Humidity Record =", csv_humi)

# SENSE: Write Humidity CSV Record
with open(path_h, "a") as log:
    log.write("\n")
    log.write(csv_humi)
    log.close()

# SENSE: Ready
print("SENSE Record Generated")
