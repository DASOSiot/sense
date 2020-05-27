#!/usr/bin/env python3

# IMPORT
import sys
import time
import pandas as pd

# ARGUMENTS
vid = "vid-000" # TODO: Replace with argument VID

# LOG: Fix
log_base = "/var/log/dasos/sense/" # Absolute Folder
log_prefix = time.strftime("%Y-%m-") # Time Prefix
sl = "cron-sense.csv" # SL = Sense Log
pl = "cron-sense.csv" # PL = Pulse Log
sp = log_base + vid + "/" + log_prefix + sl # SP = Sense Path
pp = log_base + vid + "/" + log_prefix + pl # PP = Pulse Path

# DATAFRAME: Pulse Log. Read, Write, Close.
pulse = pd.read_csv(sp)

# DATAFRAME: Pulse Log. Tail.
pulse = pulse.tail(15) # TODO: Replace "15" with argument PULSE
pulse.columns = ['t', 'v']

# PULSE: Variables
p_time = pulse["t"].mean()
print("Time =", p_time)

p_mean = pulse["v"].mean()
print("Mean =", p_mean)

p_count = pulse["v"].count()
print("Count =", p_count)

p_std = pulse["v"].std()
print("STD =", p_std)

p_min = pulse["v"].min()
print("Min =", p_min)

p_max = pulse["v"].max()
print("Max =", p_max)

# PULSE: CSV Record
csv = f"{p_time},{p_mean},{p_std},{p_min},{p_max},{p_count}"
print("CSV Record =", csv)

# PULSE: Write CSV Record
with open(pp, "a") as log:
    log.write("\n")
    log.write(csv)
    log.close()

# PULSE: Ready
print("Pulse Record Generated")
