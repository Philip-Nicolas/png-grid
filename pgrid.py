import png
import math
import sys
import cmd
from collections import namedtuple
from Pathspec import Pathspec

Pixel = namedtuple('Pixel', 'x y r g b a')

def getPixel(x, y):
    xAddr = x * 4
    return Pixel(x, y, *pic[y][xAddr:xAddr+4])

def savePixel(p):
    xAddr = p.x * 4
    pic[p.y][xAddr+0] = p.r
    pic[p.y][xAddr+1] = p.g
    pic[p.y][xAddr+2] = p.b
    pic[p.y][xAddr+3] = p.a

def t(n):
    return (255 - n) // 2

original = Pathspec(sys.argv[1], 'png')
final = Pathspec(original.directory + original.name + '_with_grid.png')

info = png.Reader(original.path).asRGBA()
width, height = info[0:2]

print('\nOriginal Image Details')
print('input file: \t%s' % original)
print('dimensions: \t%dpx by %dpx' % (width, height))

print('\nSpecify Grid Dimensions')
sqIn = input('square grid? (y/n) > ')
squareGrid = True if sqIn == '' else sqIn.lower().startswith('y')

cols = int(input('number of columns  > '))
dx = width / cols

if squareGrid:
    dy = height/round(height/dx)
else:
    rows = int(input('number of rows     > '))
    dy = height / rows

pic = list(info[2])

for y in range(1, height-1):
    for x in range(1, width-1):
        if math.floor(y % dy) == 0 or math.floor(x % dx) == 0:
            p = getPixel(x, y)
            savePixel(Pixel(x, y, t(p.r), t(p.g), t(p.b), 255))

img = png.from_array(pic, 'RGBA')
img.save(final.path)

print('\nFinal Image Details')
print('output file:  \t%s' % final.path)
print('grid spacing: \t%dpx by %dpx' % (dx, dy))
print('squareness:   \t%d%%' % round(dx*100/dy))
