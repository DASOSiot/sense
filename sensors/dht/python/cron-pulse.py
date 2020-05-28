#!/usr/bin/env python3

# IMPORT
import sys
import time
import pandas as pd

# ARGUMENTS
# 0 = Script
# 1 = Variale ID (VID)
# 2 = Cycle (minutes)

#print(f"SCRIPT = {sys.argv[0]} (filename)")

# ARGUMENTS
script = sys.argv[0]
print ("SCRIPT (filename) =",script)
vid = sys.argv[1]
print ("VARIABLE (vid) =",vid)
cycle = int(sys.argv[2])
print ("CYCLE (minutes) =",cycle)

# LOG: Fix
log_prefix = time.strftime("%Y-%m-") # Time Prefix
sp = "/var/log/dasos/sense/" + vid + "/" + log_prefix + "cron-sense.csv" # SP = Sense Path
pp = "/var/log/dasos/sense/" + vid + "/" + log_prefix + "cron-pulse-" + sys.argv[2] + ".csv" # PP = Pulse Path
print ("SENSE (path) =",sp)
print ("PULSE (path) =",pp)

# DATAFRAME: Pulse Log. Read, Write, Close.
pulse = pd.read_csv(sp)

# DATAFRAME: Pulse Log. Tail.
pulse = pulse.tail(n = cycle)
pulse.columns = ['t', 'v']

# PULSE: Variables
p_time = pulse["t"].mean()
print("TIME (unix ms) =", p_time)

p_count = pulse["v"].count()
print("COUNT (records) =", p_count)

p_mean = pulse["v"].mean()
print("MEAN =", p_mean)

p_std = pulse["v"].std()
print("STD =", p_std)

p_min = pulse["v"].min()
print("MIN =", p_min)

p_max = pulse["v"].max()
print("MAX =", p_max)

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
