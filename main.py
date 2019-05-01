import numpy as np
# Working without numpy ?
import cv2

name = "dog.jpg"
path = "img/"+name
scale = 40 # La largeur & hauteur des nouveaux 'pixels'

img = cv2.imread(path, cv2.IMREAD_COLOR)

height, width, channels = img.shape

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

cv2.imwrite('modif_'+name, img)
cv2.imshow('modif_'+name,img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ajout
# Possibilité de pixelisé les pixels non affecté (bords droits & bas)
# quand la taille de l'image n'est pas un multiple du scale
