# image-sketch-python

This is a python project that takes an image and convert it to a sketch image.

To achieve this, the following steps were taken:
- Find an image you want to convert to a sketch
- Read the image in RGB and convert to grayscale
- Invert the grayscale image, used for enhancing edges and details
- Blur the inverted grayscale image, used for smoothening the image using a Gaussian function
- Invert the blurred image, used for enhancing edges and details
- Create a pencil sketch by blending the grayscale image with the inverted blurred image. This can be done by dividing the grayscale image by the inverted blurred image.

Libraries used in this Project:
- OpenCV

Run this project in your IDE with Python 3 installed and OpenCV installed.
To install OpenCV, run *pip install opencv-python*.

Add an image file, rename to "image.jpg" in the same directory or replace existing image with your desried image

Execute the sketch.py progam in your terminal:
- python3 sketch.py
