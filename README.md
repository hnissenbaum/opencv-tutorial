# OpenCV Tutorial
This is the code for the OpenCV Tutorial that was run internally for the Queen's AutoDrive Team

## What is OpenCV?
OpenCV is a library for functions that are aimed at classical computer vision. Most real time computer vision processing that uses classical techniques will revolve around OpenCV functions, so it's important to be comfortable with it for our purposes. 

Classical Computer vision techniques rely on the intensity of pixels in the image, and use a number of predefined algorithms to extract information from images. 

## Downloading OpenCV
You can easily download OpenCV with pip using the command:

`python -m pip opencv-python `

Then you can run:
` python -m pip list `
to check that it was installed correctly. 

## Image Storage
Images are stored in mat which is short for 'matrix'. Each pixel intensity is stored in a single cell, and has an intensity value of 0-255. Intensity values must be integers and cannot be negative. 0 is always black, or 'off', and 255 is always 'on'.

Black and white images are made up of greyscale pixels ranging from white (value 255) to black (value 0).

Colour images, however are made up of three channel mats, red, green and blue (where the acronym you may have heard - RGB comes from). The three mats are layered on top of eachother at different intensity values to create the coloured images you see on screen. 

Below is a visualization of a colour image's pixels:
![Image Pixels](./imgs/image_pixels.png)


## Inputing Images and Accessing Properties 


To import OpenCV into a script, use the command: `import cv2 ` just like any other library. 

Like with other external libraries, to access OpenCV functions, you need to first tell the compiler that you want to enter that library of functions. To do so, type `cv2.function()`.

To get an image into your script use imread: `img = cv2.imread('filename')`. This function outputs an image mat, so I've named my inputed image 'img'. To input a greyscale image - you can use `cv2.imread('filename',0)`.

Here are some important functions for accessing image properties:
### shape
`img.shape` - which outputs a tuple (python list - object with multiple values), the rows, columns and channels (height, width, depth of the matrix) of the image. When the image is greyscale there is only one channel, so the image shape will only contain two values. 
### size
`img.size` - outputs the total number of pixels in the image (rows*columns)
### dtype
`img.dtype` - the dtype property is the image’s data type. It's often important to know this property, as a large 
number of errors in OpenCV can result from incorrect use of the data types. 

### imread

` cv2.imread('filename')` - gets an image into your script from a file in the same folder (use `.\containing folder\'filename'` to input an image in a different folder).

### imshow
`cv2.imshow('windowname',img)` - takes the window name that you want the image to open in (this does not need to be defined beforehand, it will create a new window if one with that name does not exist), and the image and will display the image in a seperate window. 

