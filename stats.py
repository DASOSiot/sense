# IMPORT: Dependencies
import pandas as pd
import time

# LOG: Read
df = pd.read_csv("/var/log/dasos/vid.csv")
pulse = df.tail(15)

# Pulse MEAN
p_mean = pulse["v"].mean()
print(p_mean)

# Pulse STD
p_std = pulse["v"].std()
print(p_std)

# Pulse MIN
p_min = pulse["v"].min()
print(p_min)

# Pulse Max
p_max = pulse["v"].max()
print(p_max)

# Pulse Count
p_count = pulse["v"].count()
print(p_count)

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
v = p_mean
print("Mean =", v)

# senML: CONSTRUCT
senml = f"{{\"n\":\"{n}\",\"u\":\"{u}\",\"t\":{t!r},\"v\":{v!r}}}"
print("SenML =", senml)

# LOG:WRITE
# Open the file in append ('a')
with open("/var/log/dasos/vid-stats.csv", "a") as log:
# Open the file in append & read mode ('a+')
#with open("/var/log/dasos/vid.csv", "a+") as log:
    # Append text at the end of file
    log.write(csv) # senml or csv
    #log.write("\n")
    log.close()

print("SenML Record Generated")
