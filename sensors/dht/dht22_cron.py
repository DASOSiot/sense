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
dhtDevice = adafruit_dht.DHT22(board.D5)

# senML: Name (VID)
n = "vid000"
print("Name =", n)

# senML: Unit (VID)
u = "Cel"
print("Unit =", u)

# senML: Time (UNIX MS)
t = time.time()
print("Time =", t)

# senML: Value
# Print the values to the serial port
v = dhtDevice.temperature
print("Value =", v)

# senML: CONSTRUCT
senml = f"{{\"n\":\"{n}\",\"u\":\"{u}\",\"t\":{t!r},\"v\":{v!r}}}"
print("SenML =", senml)

# LOG:WRITE
# Open the file in append ('a')
with open("/var/log/dasos/vid.log", "a") as log:
# Open the file in append & read mode ('a+')
#with open("/home/yei/Repo/github/dasosiot/sense/data/test.log", "a+") as log:
    log.write("\n")
    # Append text at the end of file
    log.write(senml)
    log.close()

print("SenML Record Generated")
