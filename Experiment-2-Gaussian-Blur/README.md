
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Upload the original image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read the image
image = cv2.imread(filename)

if image is not None:
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image, (15, 15), 0)

    # Convert images to RGB for display
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    blurred_rgb = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)

    # Display both images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(blurred_rgb)
    plt.title("Gaussian Blur")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig("output.png", bbox_inches="tight")
    plt.show()

    # Save the blurred image
    cv2.imwrite("gaussian_blur.jpg", blurred)

    print("Gaussian Blur completed successfully!")
else:
    print("Error: Unable to read the image.")
