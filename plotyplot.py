#   P L O T Y P L O T v1.1   #
# random version numbers yay #
# Gustavo Santiago,  8937416 #
import cv2
import numpy as np

#Normalization function (for functions that overflows 255)
def normalizeRGB(resRGB, size):
    return (resRGB/(2 * size)) * 255

#Program functions
def calcRGB(size, xRGB, yRGB, q, funcnum):
    resRGB = 0
    if(funcnum == 1):
        #f(x, y) = (x + y)
        resRGB = xRGB + yRGB
        resRGB = normalizeRGB(resRGB, size)
    elif(funcnum == 2):
        #f(x, y) = |sin(x, q) * 255|
        resRGB = np.absolute(np.sin(xRGB/q) * 255)
    elif(funcnum == 3):
        #f(x, y) = |(x/q)^2 + 2*(y/q)^2| * 255
        resRGB = np.absolute(np.power(xRGB/q, 2) + 2 * np.power(yRGB/q, 2))/255
    elif(funcnum == 4):
        #f(x, y) = rand(0, 255)
        resRGB = np.random.randint(0, 255)
    return resRGB

#Functions' loop, iterating through the image's pixels
def functionLoop(image, size, q, funcnum):
    for x in range(0, size):
        for y in range(0, size):
            #Calculating f(x, y)...
            resRGB = calcRGB(size, x, y, q, funcnum)
            #Filling the pixels...
            image[x,y] = (resRGB)
    return image

#main#
#----------------------------------------------------------------------#
#Splashscreen :D
print("### P L O T Y P L O T v1.1 ###")

filename = input("Type in the output filename (w/o filetype): ")
if(len(filename) == 0):
    filename = "output"
filename += ".png"

size = input("Type in the image resolution (in px): ")
size = int(size)
if(size <= 0):
    print("Invalid size :(")
else:
    funcnum = input("Type in the function number (1-4): ")
    funcnum = int(funcnum)
    if(funcnum < 1 or funcnum > 4):
        print("Invalid function :(")
    else:
        if(funcnum != 1 and funcnum != 4):
            q = input("Type in the frequency parameter (Q): ")
            q = int(q)
        else:
            q = 1

        output = np.zeros((size, size, 1), np.uint8)
        output = functionLoop(output, size, q, funcnum)

        cv2.imshow('plotyplot_output', output)
        cv2.imwrite(filename, output)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
print("Closing program...")
#----------------------------------------------------------------------#
