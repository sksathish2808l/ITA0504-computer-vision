import cv2
from google.colab.patches import cv2_imshow

image = cv2.imread("sample.jpg") # Replace with your image file
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200) # 100 and 200 are threshold values

print("Original Image:")
cv2_imshow(image)

print("Edge Detected Image:")
cv2_imshow(edges)
