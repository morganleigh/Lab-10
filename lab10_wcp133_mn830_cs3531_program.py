# Lab 10

from PIL import Image
img = Imgage.open( "handprint.png" )

img = img.convert( "L" )

# image dimesnions 
cols = img.size[0] #width
rows = img.size[1] #height

pix = img.load()

print( "pixel at row", 3, "and col", 4, "is", pix[4, 3] )

for row in range(rows):
  for col in range(cols):
    pix [col, row] = 255 - pix[ col, row ]

print( "Hi" )

print( "don't even know what I'm doing" )
