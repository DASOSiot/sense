#!/usr/bin/env python3

# IMPORT
import sys
import time
import pandas as pd

# TODO: Replace "vid-000" with argument VID
#
# LOG: Fix, Global
prefix = time.strftime("%Y-%m-")
path = "/var/log/dasos/sense/"
vid = "vid-001"

# LOG: Fix, Sense
# SL = Sense Log
sl = "cron-sense.csv"
# SP = Sense Path
sp = "/var/log/dasos/sense/" + vid + "/" + prefix + sl

# LOG: Fix, Pulse
# PL = Pulse Log
pl = "cron-sense.csv"
# SP = Pulse Path
pp = "/var/log/dasos/sense/" + vid + "/" + prefix + sl

# DATAFRAME: Pulse Log. Read, Write, Close.
pulse = pd.read_csv(sp)

# TODO: Replace "15" with argument PULSE
#
# DATAFRAME: Pulse Log. Tail.
pulse = pulse.tail(15)
pulse.columns = ['t', 'v']

# PULSE: Variables

p_time = pulse["t"].mean() # Pulse TIME
print("Time =", p_time)

p_mean = pulse["v"].mean() # Pulse MEAN
print("Mean =", p_mean)

p_count = pulse["v"].count() # Pulse COUNT
print("Count =", p_count)

p_std = pulse["v"].std() # Pulse STD
print("STD =", p_std)

p_min = pulse["v"].min() # Pulse MIN
print("Min =", p_min)

p_max = pulse["v"].max() # Pulse Max
print("Max =", p_max)

# RECORD: CSV
csv = f"{p_time},{p_mean},{p_std},{p_min},{p_max},{p_count}" # String Composition
print("Record =", csv)

# DATAFRAME: Pulse Log. Read, Write, Close.
with open(pp, "a") as log: # Open the file in append ('a')
    log.write("\n") # Append Line
    log.write(csv) # Append Record
    log.close() # LOG: Close

# PULSE: Ready
print("Pulse Record Generated")
