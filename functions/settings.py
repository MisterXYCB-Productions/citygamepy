from time import sleep
import keyboard
import os

from classes.settings import settings

clear = lambda: os.system('cls')

def changeSettings():
    sleep(0.05)
    clear()
    print("Welche Einstellung möchtest du ändern?\n\n1. Bundesland wird angezeigt: " + str(settings.bundesland) + "\n2. Einwohnerzahl wird angezeigt: " + str(settings.einwohner) + "\n3. Es werden nur Städte über 100 Tausend Einwohnern ausgewählt: " + str(settings.above100k) + "\n4. Runden: " + str(settings.rounds) + "\n\nDrücke z um zurückzugehen und esc um das Spiel zu beenden.")
    while True:
        if(keyboard.is_pressed("1")):
            settings.bundesland = False if settings.bundesland else True
            changeSettings()
        if(keyboard.is_pressed("2")):
            settings.einwohner = False if settings.einwohner else True
            changeSettings()
        if(keyboard.is_pressed("3")):
            settings.above100k = False if settings.above100k else True
            changeSettings()
        if(keyboard.is_pressed("4")):
            clear()
            runden = input("Wie viele Runden (maxmial 10 mindestens 1)")
            settings.rounds = int(runden) if runden.isnumeric() and int(runden) < 11 and int(runden) > 0 else 5
            changeSettings()
        if(keyboard.is_pressed("esc")):
            quit()
        if(keyboard.is_pressed("z")):
            break