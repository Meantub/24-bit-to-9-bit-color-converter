# import the image module
from PIL import Image
import itertools

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)
    return rightMin + (valueScaled * rightSpan)

# Read a color image
colorImage = Image.open("./UML3.png")

# Convert using adaptive palette of color depth 8
imageWithColorPalette = colorImage.convert("P", palette=Image.ADAPTIVE, colors=9)
# imageWithColorPalette.show()

pixels = list(colorImage.getdata())
width, height = colorImage.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

sumString = "";

for y in range(32):
	for x in range(32):
		r = int(translate(pixels[y][x][0], 0, 255, 0, 7))
		g = int(translate(pixels[y][x][1], 0, 255, 0, 7))
		b = int(translate(pixels[y][x][2], 0, 255, 0, 7))
		rgb = (r,g,b)
		sumString += "matrix.drawPixel({}, {}, matrix.Color333({}, {}, {}));".format(x, y, r, g, b)

file = open("output.txt", "w")

file.write(sumString)
print(sumString)
