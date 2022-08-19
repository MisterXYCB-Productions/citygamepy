import csv
import random

if(0 == 0):
    tlat = 0
    tlatm = 0
    tlon = 0
    tlonm = 0
    tpop = 0
    

f = open("./data2.csv", "r", newline="")
csv_reader = csv.reader(f)
rows = list(csv_reader)

trows = 602

rcity = random.randint(0, trows)
rlat = float(rows[rcity] [1])
rlon = float(rows[rcity] [2])
print((rows[rcity] [0]) + " (" + (rows[rcity] [4]) + ")")

c1 = int(input("Stadt auswählen: "))
if(c1 > trows):
    print("Error: Eingabe muss unter " + str(trows) + " sein!")
    c1 = int(input("Stadt auswählen: "))
c2 = int(input("Stadt auswählen: "))
if(c2 > trows):
    print("Error: Eingabe muss unter " + str(trows) + " sein!")
    c2 = int(input("Stadt auswählen: "))

if(c1 > trows or c2 > trows):
    quit()

c1lat = float(rows[c1] [1])
c1lon = float(rows[c1] [2])

c2lat = float(rows[c2] [1])
c2lon = float(rows[c2] [2])

c12 = 1
latde = c1lat - c2lat
londe = c1lon - c2lon

if(latde < 0):
    c12 = 2
    latde = latde *-1
    londe = londe *-1

print(latde)
print(londe)

latde1 = latde / latde
londe1 = londe / latde

print(latde1)
print(londe1)

if(c12 == 1):
    latdecr = c1lat - rlat
elif(c12 == 2):
    latdecr = c2lat - rlat
cplat = latdecr * latde1