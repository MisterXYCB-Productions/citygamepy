import csv

f = open("./data2.csv", "r", newline="")
csv_reader = csv.reader(f)
rows = list(csv_reader)

#Searching the data for a city with the name
def findCityByName(name):
    if(name in ["Bayern", "Nordrhein-Westfalen", "Hessen", "Baden-Wuerttemberg", "Sachsen", "Niedersachsen", "Schleswig-Holstein", "Sachsen-Anhalt", "Mecklenburg-Vorpommern", "Thueringen", "Rheinland-Pfalz", "Saarland", "Brandenburg"]):
        return None
    index = -1
    for x in rows:
        index += 1
        city = str(x[0])
        if(name.lower() == city.lower()):
            return index
        if(index > 602):
            return None
    


def getCity(var, cityNumber):
    cityByName = findCityByName(var)
    if(cityByName is not None):
        return(int(cityByName))
    elif(isinstance(var, int) and var < 602 and var > 0):
        return var
    else:
        print("Error: Input muss der Name einer deutschen Stadt sein oder eine Zahl zwischen 1 und 601")
        if(cityNumber == 1):
            return getCity(input("Stadt 1 auswählen:"), 1)
        elif(cityNumber == 2):
            return getCity(input("Stadt 2 auswählen:"), 2)
        else: 
            quit()
