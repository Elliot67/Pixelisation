import numpy as np
import cv2

name = "fleur.jpg"

img = cv2.imread(name, cv2.IMREAD_COLOR)

height, width, channels = img.shape
print(width, height)

rouge = []
vert = []
bleu = []

for x in range(width):
	for y in range(height):
		rouge.append(img[y,x][0])
		vert.append(img[y,x][1])
		bleu.append(img[y,x][2])

moyR = round(sum(rouge)/len(rouge))
moyV = round(sum(vert)/len(vert))
moyB = round(sum(bleu)/len(bleu))
print(moyR, moyV, moyB)

img[0:height, 0:width] = [moyR, moyV, moyB]

cv2.imwrite('modif_'+name, img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
