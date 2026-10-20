
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Step 1: Upload an image
uploaded = files.upload()
filename = next(iter(uploaded))

# Step 2: Read the image
image = cv2.imread(filename)

if image is None:
    print("Error: Unable to read the image.")
else:
    # Step 3: Convert the image from BGR to RGB
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Step 4: Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 5: Display both images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")

    plt.tight_layout()

    # Step 6: Save the output
    plt.savefig("output.png", bbox_inches="tight")
    cv2.imwrite("grayscale_image.jpg", gray)

    plt.show()

    print("Grayscale conversion completed successfully!")

    # Step 7: Download the output
    files.download("output.png")
    files.download("grayscale_image.jpg")
