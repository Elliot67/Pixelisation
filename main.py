import numpy as np
# Working without numpy ?
import cv2
import argparse
import math

parser = argparse.ArgumentParser(description='Pixelate an image at the scale of your choice.')
parser.add_argument('image', type=str, help='The original image file', metavar='')
parser.add_argument('-s', '--scale', type=int, default=0, help="The number of pixel for your new pixel.", metavar='')
parser.add_argument('-o', '--output', type=str, default=0, help="The name of the outputted image", metavar='')
args = parser.parse_args()

name = args.image

if not args.output:
	output = name.replace('.', '_pixelate.')
else:
	output = args.output

img = cv2.imread(name, cv2.IMREAD_COLOR)
height, width, channels = img.shape

if args.scale <= 0:
	scale = math.ceil(min(height, width)/30)
else:
	scale = args.scale

newHeight = int(height/scale)
newWidth = int(width/scale)

print(width, height)
print(newWidth, newHeight)

def moyenne(tab):
	return int(round(sum(tab)/len(tab)))

for x in range(newWidth):
	x = x * scale
	for y in range(newHeight):
		y = y * scale
		spotR = []
		spotV = []
		spotB = []
		for spotX in range(scale):
			for spotY in range(scale):
				spotR.append(img[y+spotY,x+spotX][0])
				spotV.append(img[y+spotY,x+spotX][1])
				spotB.append(img[y+spotY,x+spotX][2])
		spotR = moyenne(spotR)
		spotV = moyenne(spotV)
		spotB = moyenne(spotB)
		img[y:y+scale, x:x+scale] = [spotR, spotV, spotB]

cv2.imwrite(output, img)
cv2.imshow(output,img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TODO: Possibilité de pixelisé les pixels non affecté (bords droits & bas)
# quand la taille de l'image n'est pas un multiple du scale
