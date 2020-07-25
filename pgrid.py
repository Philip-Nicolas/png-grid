import png
import math
import sys
import cmd
from collections import namedtuple

Pixel = namedtuple('Pixel', 'r g b a')
class Pathspec:
    def __init__(self, pathspec, defaultExtension = None):
        if '/' in pathspec:
            self.directory = pathspec[0:pathspec.rfind('/')]
            self.directory += '/' if not self.directory.endswith('/') else ''
            dirent = pathspec.split('/').pop()
        else:
            self.directory = ''
            dirent = pathspec

        if '.' in dirent:
            self.name, _, extension = dirent.rpartition('.')
            self.extension = '.' + extension
        else:
            self.name = dirent
            self.extension = ''
        
        if defaultExtension is not None and self.extension == '':
            self.extension = defaultExtension if '.' in defaultExtension else '.' + defaultExtension

        self.path = self.directory + self.name + self.extension
        self.filename = self.name + self.extension

    def __str__(self):
        return self.path

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
    return (255 - n) // 2

original = Pathspec(sys.argv[1], 'png')
final = Pathspec(original.directory + original.name + '_with_grid.png')

info = png.Reader(original.path).read()
width, height = info[0:2]

print('\nOriginal Image Details')
print('input file: \t%s' % original)
print('dimensions: \t%dpx by %dpx' % (width, height))

print('\nSpecify Grid Dimensions')
sqIn = input('square grid? (yes/no) > ')
sqIn = 'y' if sqIn == '' else sqIn
squareGrid = sqIn.lower().startswith('y')

cols = int(input('columns > '))
dx = width / cols

if squareGrid:
    dy = height/round(height/dx)
else:
    rows = int(input('rows    > '))
    dy = height / rows

pic = list(info[2])

for y in range(1, height-1):
    for x in range(1, width-1):
        if math.floor(y % dy) == 0 or math.floor(x % dx) == 0:
            p = getPixel(x, y)
            savePixel(x, y, Pixel(t(p.r), t(p.g), t(p.b), 255))

img = png.from_array(pic, 'RGBA')
img.save(final.path)

print('\nFinal Image Details')
print('output file:  \t%s' % final.path)
print('grid spacing: \t%dpx by %dpx' % (dx, dy))
if squareGrid: print('squareness:   \t%d%%' % round(dx*100/dy))
