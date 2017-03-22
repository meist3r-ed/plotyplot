# **PLOTYPLOT**

Image generation assignment for IP subject at college :ok_hand:

>   as requested by professor Moacir Ponti


## **USAGE**

The program requires the OpenCV library for matrix operations and image generation, and numpy for function operations.

It can be simply run from a properly configured Windows cmd or Linux terminal, just head to the project's folder and type:

>   python plotyplot.py

## **FUNCTIONS**

There are 4 mathematical functions for image generation, you can choose one per execution and tweak the Q parameter

* f(x, y) = (x + y)
* f(x, y) = |sin(x, q) * 255|
* f(x, y) = |(x/q)^2 + 2*(y/q)^2| * 255
* f(x, y) = rand(0, 255)

Values returned from f(x, y) are then assigned into the matrix as RGB values, with the following format:

>   matrix[x, y] = (result)

The resulting image is a greyscale .png based on the chosen function
