import cv2
import numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread("sample.jpg") 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)

print("Original Grayscale Image:")
cv2_imshow(gray_image)

print("Histogram Equalized Image:")
cv2_imshow(equalized_image)
