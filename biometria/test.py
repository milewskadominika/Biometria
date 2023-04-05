#edycja i zapis nowego obrazu - rozciąganie histogramu

import numpy as np
import cv2


picture = cv2.imread('hill.jpg', 0)
hist = np.zeros(256)


for i in range(len(picture)):
    for j in range(len(picture[0])):
        if picture[i][j] !=0:
            hist[picture[i][j]] +=1

minValue = 0
maxValue = 255
newpicture = np.zeros((len(picture), len(picture[0])))

for i in range(0,256):
    if(hist[i] != 0):
        minValue = i
        break

for i in range(255,-1,-1):
    if(hist[i] != 0):
        maxValue = i
        break

for i in range(len(picture)):
    for j in range(len(picture[0])):
       newpicture[i][j]=((255 / (maxValue - minValue))*(picture[i][j] - minValue))


cv2.imwrite('newpicture.png', newpicture)

