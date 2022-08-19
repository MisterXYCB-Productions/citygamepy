import numpy

def getOffsetDistance(x1, y1, x2, y2, x3, y3):
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    d = numpy.cross((p2-p1), (p1-p3))/numpy.linalg.norm(p2-p1)
    print(d)
    return d
