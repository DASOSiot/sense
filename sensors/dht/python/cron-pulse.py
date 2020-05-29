#!/usr/bin/env python3

# IMPORT
import sys
import time
import pandas as pd

# ARGUMENTS: Definitions
print (f"SCRIPT (file): {sys.argv[0]}")
print (f"VARIABLE (vid): {sys.argv[1]}")
print (f"CYCLE (minutes): {sys.argv[2]}")

# ARGUMENTS: Transformations
cycle = int(sys.argv[2])

# LOG: Variables
log_prefix = time.strftime("%Y-%m") # Time Prefix
sp = f"/var/log/dasos/sense/{sys.argv[1]}/{log_prefix}-cron-sense.csv" # SP = Sense Path
print ("SENSE (path) =",sp)
pp = f"/var/log/dasos/sense/{sys.argv[1]}/{log_prefix}-cron-pulse-{sys.argv[2]}.csv" # # PP = Pulse Path
print ("PULSE (path) =",pp)

# DATAFRAME: Tail Pulse Log.
pulse = pd.read_csv(sp)
pulse = pulse.tail(n = cycle)
##
# TODO
pulse.columns = ['t', 'v']
# TODO
##

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
