# Rieser,Alix , Molchanova, Aleksandra, Lama,Christopher
import cv2
from datetime import datetime

def diff(img1, img2, saveLocation):
    # Load the two images
    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)

    # Resize the images to have the same dimensions
    if image1.shape != image2.shape:
        image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

    # Find the absolute difference between the two images
    difference = cv2.absdiff(image1, image2)

    # Display the difference image
    cv2.imwrite(f"{saveLocation}\\"+"Final_" + str(datetime.now()).replace(" ", "_").replace("-","_").replace(":","_") + ".jpg", difference)

