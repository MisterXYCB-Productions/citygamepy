from time import sleep
import keyboard
from classes.points import points

from functions.start import startMenu

def end():
    score = points.one + points.two + points.three + points.four + points.five + points.six + points.seven + points.eight + points.nine + points.ten
    print("Über die " + str(points.round) + "(e) Runde(n) hast du insgesamt " + str(score) + "[einheit] abweichung gehabt.")

    print("Drücke die Leertaste um fortzufahren.")
    while True:
        if(keyboard.is_pressed("space")):
            sleep(0.05)
            startMenu()
            break
