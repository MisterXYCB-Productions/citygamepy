import keyboard
from classes.points import points

from functions.settings import changeSettings

def startMenu():
    print("Drücke die Leertaste um das Spiel zu starten, drücke \"s\" um in die Einstellungen zu gehen, drücke esc um das Spiel zu beenden.")
    while True:
        if(keyboard.is_pressed("space")):
            points.one = 0
            points.two = 0
            points.three = 0
            points.four = 0
            points.five = 0
            points.six = 0
            points.seven = 0
            points.eight = 0
            points.nine = 0
            points.ten = 0
            points.round = 0
            break
        if(keyboard.is_pressed("esc")):
            quit()
        if(keyboard.is_pressed("s")):
            changeSettings()
            startMenu()