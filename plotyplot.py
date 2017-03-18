#   P L O T Y P L O T v0.0   #
# Gustavo Santiago,  8937416 #
import cv2
import numpy as np

def valRGB(seed, num):
    x = (255 * num)/seed
    return num

def function(image, size, q, funcnum):
    for x in range(0, size):
        for y in range(0, size):
            xRGB = valRGB(size, x)
            yRGB = valRGB(size, y)
            if(funcnum == 1):
                resRGB = xRGB + yRGB
            if(funcnum == 2):
                resRGB = np.absolute(np.sin(xRGB/q) * 255)
            image[x,y] = (resRGB, resRGB, resRGB)

    return image

print("### P L O T Y P L O T v0.0 ###")
filename = input("Type in the output filename (w/o filetype): ")
filename += ".png"
size = input("Type in the image resolution (in px): ")
size = int(size)
q = input("Type in the frequency parameter (Q): ")
q = int(q)

funcnum = 2

output = np.zeros((size, size, 3), np.uint8)
output = function(output, size, q, funcnum)

cv2.imshow('output', output)
cv2.imwrite(filename, output)

cv2.waitKey(0)
cv2.destroyAllWindows()
