#!/usr/bin/env python3

# IMPORT: Dependencies
import pandas as pd

# DATAFRAME: Read File
df = pd.read_csv("/var/log/dasos/sense/vid-001/cron-sense.csv")
# DATAFRAME: Tail Data Set
pulse = df.tail(15)

# PULSE: Variables
# Pulse TIME
p_time = pulse["t"].mean()
print("Time =", p_time)
# Pulse MEAN
p_mean = pulse["v"].mean()
print("Mean =", p_mean)
# Pulse COUNT
p_count = pulse["v"].count()
print("Count =", p_count)
# Pulse STD
p_std = pulse["v"].std()
print("STD =", p_std)
# Pulse MIN
p_min = pulse["v"].min()
print("Min =", p_min)
# Pulse Max
p_max = pulse["v"].max()
print("Max =", p_max)

# RECORD: CSV
csv = f"{p_time},{p_mean},{p_std},{p_min},{p_max},{p_count}" # String Composition
print("Record =", csv)

# PULSE: Open, Write, Close
with open("/var/log/dasos/sense/vid-001/cron-pulse.csv", "a") as log: # Open the file in append ('a')
    log.write("\n") # Append Line
    log.write(csv) # Append Record
    log.close() # LOG: Close

# PULSE: Ready
print("Pulse Record Generated")
