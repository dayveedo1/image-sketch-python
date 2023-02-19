# This project convert an image to a sketch using opencv


#Libraries used
# - OpenCV

# STEPS
# - Find an image you want to convert to a sketch
# - Read the image in RGB and convert to grayscale
# - Invert the grayscale image, used for enhancing edges and details
# - Blur the inverted grayscale image, used for smoothening the image using a Gaussian function
# - Invert the blurred image, used for enhancing edges and details
# - Create a pencil sketch by blending the grayscale image with the inverted blurred image. This can be done by dividing the grayscale image by the inverted blurred image.

import cv2                                                                                  # import opencv library

image = cv2.imread('image.jpg')                                                             # read image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                        # convert image to gray scale
cv2.imwrite('gray_image.jpg', gray_image)                                                   # save image
inverted_image = 255 - gray_image                                                           # invert image
cv2.imwrite('inverted_image.png', inverted_image)                                           # save image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)                                     # blur image
cv2.imwrite('blurred.png', blurred)                                                         # save image
inverted_blurred = 255 - blurred                                                            # invert blurred image
cv2.imwrite('inverted_blurred.png', inverted_blurred)                                       # save image

pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)                       # divide image by inverted blurred image
cv2.imwrite('sketch.png', pencil_sketch)                                                    # save image
