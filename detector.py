# Author: Ashok Saravanan
# Created: 04/04/2022

import cv2
import numpy as np
import math
MT = cv2.imread('MTB.jpg')
WT = cv2.imread('WTB.jpg')
imgs = [MT, WT]
dims = [[611, 605, 569], [620, 625, 589]]
crops = []
out = 'start'

for img, dim in zip(imgs, dims):
    height, width = img.shape[0:2]
    mask = np.zeros((height, width), np.uint8)
    circle_img = cv2.circle(mask, (dim[0], dim[1]), dim[2], (255, 255, 255), thickness=-1)
    crop = cv2.bitwise_and(img, img, mask=circle_img)

    crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    crop = cv2.bitwise_not(crop)

    crop1 = crop[0:height, 0:dim[0]]
    crop2 = crop[0:height, dim[0]:width]

    if out == "MT":
        out = "WT"
    else:
        out = "MT"
    var = 135
    area = np.sum(crop1) - 255 * ((width / 2) * (height) - 0.5 * math.pi * (dim[2] ** 2))
    percent = area / (var * 0.5 * math.pi * (dim[2] ** 2))
    percent = f"{percent:.0%}"

    print(out + ' percentage without bug spray: ' + percent)

    area = np.sum(crop2) - 255 * ((width / 2) * (height) - 0.5 * math.pi * (dim[2] ** 2))
    percent = area / (var * 0.5 * math.pi * (dim[2] ** 2))
    percent = f"{percent:.0%}"

    print(out + ' percentage with bug spray: ' + percent + '\n')

    cv2.circle(img, (dim[0], dim[1]), dim[2], (0, 255, 0), 4)
    cv2.rectangle(img, (dim[0] - 5, dim[1] - 5), (dim[0] + 5, dim[1] + 5), (0, 128, 255), -1)
    cv2.line(img, (dim[0], dim[1]-dim[2]), (dim[0], dim[1]+dim[2]), (0, 255, 0), 4)

    crop = cv2.cvtColor(crop, cv2.COLOR_GRAY2BGR)
    cv2.circle(crop, (dim[0], dim[1]), dim[2], (0, 255, 0), 4)
    cv2.rectangle(crop, (dim[0] - 5, dim[1] - 5), (dim[0] + 5, dim[1] + 5), (0, 128, 255), -1)
    cv2.line(crop, (dim[0], dim[1] - dim[2]), (dim[0], dim[1] + dim[2]), (0, 255, 0), 4)

    crops.append([img, crop, crop1, crop2])

for image in enumerate(crops):
    if image[0] == 0:
        out = 'MT'
    else:
        out = "WT"
    for img in enumerate(image[1]):
        cv2.imwrite('images/' + out + str(img[0]+1) + '.jpg', img[1])

cv2.imshow('result', crops[1][3])
cv2.waitKey(0)


#crop3 = crops[1][1][100:150, 100:150]
#print(crop3)
