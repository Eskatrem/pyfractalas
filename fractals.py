#!/usr/bin/python

import Image, ImageDraw
from math import cos, sin, pi
W = 255
H = 128

img = Image.new("RGB", (W, H), "black")
draw = ImageDraw.Draw(img)

def drawLine(a,b):
    draw.line([(a.x,a.y),(b.x,b.y)])



class vector2d():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self, vect):
        return vector2d(self.x+vect.x, self.y+vect.y)
    def tuple(self):
        return (self.x, self.y)

class Shape():
    def __init__(self, edges):
        self.edges = edges
    def draw(self):
       nEdges = self.edges.length
       for i in range(nEdges):
           if i == (nEdges-1):
               j = 0
           else:
               j = i+1
           a = self.edges[i]
           b = self.edges[j]
           drawLine(a,b) #TODO: implement drawLine


           


def getPoints(center, side, angle):
    a = center+vector2d(-side*cos(angle), -side*sin(angle))
    c = center+vector2d(side*cos(angle), side*sin(angle))
    return a,c


def draw_square(center, side, angle, color = "#FF00FF"):
    pMin, pMax = getPoints(center, side, angle)
    draw.rectangle([pMin.tuple(), pMax.tuple()], outline=color)
    
def getEdges(center, side, angle):
    a = center+vector2d(-side*cos(angle), -side*sin(angle))
    b = center+vector2d(-side*cos(angle), side*sin(angle))
    c = center+vector2d(side*cos(angle), side*sin(angle))
    d = center+vector2d(side*cos(angle), -side*sin(angle))
    return [a,b,c,d]


def draw_fractal(n_iter):
    k = 0
    edges = [vector2d(122,64)]
    side = 80
    angle = pi/4
    r,g,b = 15,117,213
    color = (r,g,b)
    while k < n_iter:
        new_edges = []
        side = side/2    
        for edge in edges:
            new_edges += getEdges(edge, side, angle)
            draw_square(edge, side, angle,color=color)
        
        r = r*2 %255
        g = g*3%255
        b = b*4 %255
        color = (r,g,b)
        edges = new_edges
        k += 1
        img.save("test_fractal"+str(k)+".png", "PNG")

def draw_test():
    for x in range(W):
        for y in range(H):
            color = (x % 255, y % 255, (x % (y+1)) % 255)
            draw.point((x,y), fill=color)

    draw.line((0, H/2, W, H/2), "yellow")
    draw.rectangle([(200, 60), (100, 120)], outline="#FF00FF")
    draw.text((20, 40), "quickies.seriot.ch")

    img.save("img.png", "PNG")

if __name__ == "__main__":
    #draw_test()
    #draw_fractal(5)#vector2d(122,64),80,pi/4)
    drawLine(vector2d(10,10),vector2d(100,100))
    draw.arc((10,10,100,50),0,360)
    img.save("test_line.png","PNG")
