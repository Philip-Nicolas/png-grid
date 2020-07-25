import png
import math
import sys
import cmd
from collections import namedtuple

Pixel = namedtuple('Pixel', 'r g b a')

def getPixel(x, y):
    x *= 4
    return Pixel(*pic[y][x:x+4])

def savePixel(x, y, p):
    x *= 4
    pic[y][x+0] = p.r
    pic[y][x+1] = p.g
    pic[y][x+2] = p.b
    pic[y][x+3] = p.a

def t(n):
    return (255 - n) // 3

pathToOriginal = sys.argv[1]

print('Reading original: ' + pathToOriginal)
info = png.Reader(pathToOriginal).read()

width, height = info[0:2]
print('Size (pixels): %d by %d' % (width, height))

gridCols = int(input('columns > '))
gridRows = int(input('rows    > '))

pic = list(info[2])

xInterval = width / gridCols
yInterval = height / gridRows

print('X-Interval: %d' % xInterval)
print('Y-Interval: %d' % yInterval)

for y in range(1, height-1):
    for x in range(1, width-1):
        if math.floor(y % yInterval) == 0 or math.floor(x % xInterval) == 0:
            p = getPixel(x, y)
            savePixel(x, y, Pixel(t(p.r), t(p.g), t(p.b), 255))

img = png.from_array(pic, "RGBA")
img.save("res.png")
