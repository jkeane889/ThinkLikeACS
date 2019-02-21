# Chp16. Execise 1
import math


class Point:

    def __init__(self, initX, initY):
        '''Create a new point at the given coordinates'''
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x= " + str(self.x) + ", y= " + str(self.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def distanceFromPoint(self, pointx, pointy):
        dfp = math.sqrt(((pointx - self.x)**2) + ((pointy - self.y)**2))
        return dfp

    def reflect_x(self):
        newy = (self.y * -1)
        newx = self.x
        return (newx, newy)

    def slopeFromOrigin(self):
        try:
            originx = 0
            originy = 0
            slope = ((self.y - originy) / (self.x - originx))
            return slope
        except ZeroDivisionError:
            return None

    def get_line_to(self, findx, findy):
        try:
            slope = ((self.y - findy) / (self.x - findx))
            c = findy - ((slope) * findx)
            return (slope, c)
        except ZeroDivisionError:
            return None


p = Point(0, 4)
q = Point(5, 12)
print(p.get_line_to(0, 3))
