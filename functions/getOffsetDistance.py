from math import sqrt

def getOffsetDistance(x1, y1, x2, y2, x0, y0):
    return abs((x2-x1)*(y1-y0)-(x1-x0)*(y2-y1))/sqrt((x2-x1)**2+(y2-y1)**2)
