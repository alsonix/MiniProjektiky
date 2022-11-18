import os, time, sys, random

def LogWrite():
    log.write("LuaOutput: ")
    log.write(CLSGNSTT+CLSGNLVL+CALLSIGN)
    log.write(" \n")
def PrintResult():
    print("LuaOutput:", CLSGNSTT+CLSGNLVL+CALLSIGN)

COUNTRY = input("Select your country: ")
LEVEL = input("Select HAM operator level: ")
HMCLSGN = int(input("How many callsigns do you want?: "))
RDTIME = float(input("Refresh time (s): "))

log = open("callsigns.log", "w")
LENGTH = 3
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
STRLST = ""
LTRBIND = True

if COUNTRY == "CZ" or COUNTRY == "cz":
    CLSGNSTT = "OK"
elif COUNTRY == "US" or COUNTRY == "us":
    CLSGNSTT = "NA"
elif COUNTRY == "RU" or COUNTRY == "ru":
    CLSGNSTT = "RS"
if LEVEL == "operator":
    CLSGNLVL = "1"
elif LEVEL == "amateur":
    CLSGNLVL = "0"
if LTRBIND:
    STRLST += LETTERS

print()
for x in range(HMCLSGN):
    CALLSIGN = "".join(random.sample(STRLST, LENGTH))
    time.sleep(RDTIME)
    LogWrite()
    PrintResult()

print()
dev = input("[Press enter to save the results to a log file] >---> (callsigns.log).") # END
log.close()
