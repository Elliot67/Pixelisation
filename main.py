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

# Define output
if not args.output:
	output = name.replace('.', '_pixelate.')
else:
	output = args.output

img = cv2.imread(name, cv2.IMREAD_COLOR)
height, width, channels = img.shape

# Define scale
if args.scale <= 0:
	scale = math.ceil(min(height, width)/30)
else:
	scale = args.scale


if (height % scale != 0) or (width % scale != 0):
	print("The entire image cannot be totally Pixelate due to its dimension")
	print("- Enter 0 to exit")
	print("- Enter 1 to automatically resize the image")
	print("- Enter 2 to automatically change the scale factor")
	print("- Enter 3 to pixelate the possible part")
	choice = input('Enter your choice and press enter : ')

	if choice == '0':
		raise SystemExit(0)
	elif choice == '1':
		# Redimensionne l'image
		print('Choix 1')
	elif choice == '2':
		# Change the scale factor
		# https://math.stackexchange.com/questions/715580/find-the-next-divisor-without-remainder
		print('Choix 2')
	elif choice == '3':
		pass
	else:
		print('Not a valid option, default option: 3')

## Fin vérification

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
