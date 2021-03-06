'''
Usage:
import Disc //from <pathToFile>
Reference:
Disc.move(self, coords)
    Translate self by given vector coords = [x, y] where x, y are floats.
Disc.rotateVector(self, angle)
    Rotate self counterclockwise through an angle = x using rotation matrix where x is a float.
'''

from math import cos, sin

class Disc:

    def __init__(self, radius=.5, coords=(0, 0)):
        self.radius = radius
        self.x = coords[0]
        self.y = coords[1]

    def __repr__(self):
        return "Disc({:.2f}, ({:.2f}, {:.2f}))".format(self.radius, self.x, self.y)

    def move(self, coords):
        self.x += coords[0]
        self.y += coords[1]

    def rotateVector(self, ang):
        x, y = self.x, self.y
        self.x = x*cos(ang)-y*sin(ang)
        self.y = x*sin(ang)+y*cos(ang)
