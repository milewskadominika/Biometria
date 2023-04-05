#wyliczanie i rysowanie histogramów obrazów przed i po edycji obrazów

import numpy as np
import matplotlib.pyplot as plt
import mahotas.demos
from pylab import imshow, show


def LUT(channel):
    minValue = 0
    maxValue = 255
    result = []

    for i in range(0,256):
        if(channel[i] != 0):
            minValue = i
            break

    for i in range(255,-1,-1):
        if(channel[i] != 0):
            maxValue = i
            break

    x = 255/(maxValue-minValue)

    for i in range(0, 256):
        value = int(x * (i - minValue))
        if value <= 0:
            result.append(0)
        else:
            result.append(value)

    return result


picture = mahotas.imread('hill.jpg')
picture = picture.astype(np.uint8)

imshow(picture)
show()
"""
plt.hist(picture[:,:,0])
plt.hist(picture[:,:,1])
plt.hist(picture[:,:,2])
plt.xlim(0,255)
plt.title("Histogram obrazu przed rozciągnięciem")
plt.xlabel("Numer odcienia")
plt.ylabel("Ilość pikseli danego koloru")
plt.show()
"""
histRed = np.zeros(256)
histGreen = np.zeros(256)
histBlue = np.zeros(256)


for i in range(len(picture)):
    for j in range(len(picture[0])):
        if picture[i][j][0] !=0:
            histRed[picture[i][j][0]] +=1

for i in range(len(picture)):
    for j in range(len(picture[0])):
        if picture[i][j][1] !=0:
            histGreen[picture[i][j][1]] +=1

for i in range(len(picture)):
    for j in range(len(picture[0])):
        if picture[i][j][2] !=0:
            histBlue[picture[i][j][2]] +=1



lutRed = LUT(histRed)
lutGreen = LUT(histGreen)
lutBlue = LUT(histBlue)



newpictureRed = np.zeros((len(picture), len(picture[0])))
newpictureGreen = np.zeros((len(picture), len(picture[0])))
newpictureBlue = np.zeros((len(picture), len(picture[0])))

for i in range(len(picture)):
    for j in range(len(picture[0])):
        newpictureRed[i][j] = lutRed[picture[i][j][0]]

for i in range(len(picture)):
    for j in range(len(picture[0])):
        newpictureGreen[i][j] = lutGreen[picture[i][j][1]]

for i in range(len(picture)):
    for j in range(len(picture[0])):
        newpictureBlue[i][j] = lutBlue[picture[i][j][2]]


newpicture = np.dstack([newpictureRed, newpictureGreen, newpictureBlue])
imshow(newpicture)
show()



plt.hist(newpictureBlue)
plt.hist(newpictureRed)
plt.hist(newpictureGreen)
plt.xlim(0,256)
plt.title("Histogram obrazu po rozciągnięciu")
plt.xlabel("Numer odcienia")
plt.ylabel("Ilość pikseli danego koloru")
plt.show()

