import csv
import random
import os
from re import A
from time import sleep
import keyboard

from classes.settings import settings
from classes.points import points
from functions.end import end
from functions.getCity import getCity
from functions.getOffsetDistance import getOffsetDistance

clear = lambda: os.system('cls')

def play():
    if(points.round == settings.rounds):
        return end()
    points.round += 1
    clear()
        
    f = open("./data/data2.csv", "r", newline="")
    csv_reader = csv.reader(f)
    rows = list(csv_reader)

    trows = 81 if settings.above100k else 602

    rcity = random.randint(0, trows)
    rlat = float(rows[rcity] [1])
    rlon = float(rows[rcity] [2])
    print((rows[rcity][0]) + (" (" + rows[rcity][3] + ")" if settings.einwohner else "") + (" [" + rows[rcity][4] + "]" if settings.bundesland else "") )

    c1 = int(getCity(input("Stadt 1 auswählen: "), 1, rows[rcity][0], rcity, None, None))

    #clear()
    print((rows[rcity][0]) + (" (" + rows[rcity][3] + ")" if settings.einwohner else "") + (" [" + rows[rcity][4] + "]" if settings.bundesland else "") )
    print("Stadt 1: " + (rows[c1][0]) + (" (" + rows[c1][3] + ")" if settings.einwohner else "") + (" [" + rows[c1][4] + "]" if settings.bundesland else "") )

    c2 = int(getCity(input("Stadt 2 auswählen: "), 2, rows[rcity][0], rcity, rows[c1][0], c1))

    #clear()
    print((rows[rcity][0]) + (" (" + rows[rcity][3] + ")" if settings.einwohner else "") + (" [" + rows[rcity][4] + "]" if settings.bundesland else "") )
    print("Stadt 1: " + (rows[c1][0]) + (" (" + rows[c1][3] + ")" if settings.einwohner else "") + (" [" + rows[c1][4] + "]" if settings.bundesland else "") )
    print("Stadt 2: " + (rows[c2][0]) + (" (" + rows[c2][3] + ")" if settings.einwohner else "") + (" [" + rows[c2][4] + "]" if settings.bundesland else "") )

    if(c1 > trows or c2 > trows):
        quit()

    c1lat = float(rows[c1] [1])
    c1lon = float(rows[c1] [2])

    c2lat = float(rows[c2] [1])
    c2lon = float(rows[c2] [2])

    offsetDistance = getOffsetDistance(c1lat, c1lon, c2lat, c2lon, rlat, rlon)
    print(rows[rcity][0] + " [" + rows[rcity][4] + "] ist von der Linie " + str(offsetDistance) + "[einheit] entfernt")
    if(points.round == 1):
        points.one = float(offsetDistance)
    if(points.round == 2):
        points.two = float(offsetDistance)
    if(points.round == 3):
        points.three = float(offsetDistance)
    if(points.round == 4):
        points.four = float(offsetDistance)
    if(points.round == 5):
        points.five = float(offsetDistance)
    if(points.round == 6):
        points.six = float(offsetDistance)
    if(points.round == 7):
        points.seven = float(offsetDistance)
    if(points.round == 8):
        points.eight = float(offsetDistance)
    if(points.round == 9):
        points.nine = float(offsetDistance)
    if(points.round == 10):
        points.ten = float(offsetDistance)
    print("Drücke die Leertaste um fortzufahren.")
    while True:
        if(keyboard.is_pressed("space")):
            sleep(0.05)
            play()
            break
