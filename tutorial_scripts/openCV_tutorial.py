"""This file is a test run using open CV. Mostly this is going through tutorials but I might play with attempting to piece together a panoramic image from multiple files"""

#Imports
import cv2 as cv
import sys

#Load an image from my computer
img = cv.imread("C:\\Users\\begin\\OneDrive\\Pictures\\Commercial Light and Magic\\Project Cid.jpg")

#Load the image as unchanged
img2 = cv.imread("C:\\Users\\begin\\OneDrive\\Pictures\\Commercial Light and Magic\\Project Cid.jpg", cv.IMREAD_UNCHANGED)

#Check if image is loaded correctly, if not, exit the program
if img is None:
    sys.exit("Could not read the image")
else:
    print("Success!")

#Show the image
cv.imshow("Display 1", img)

#Show the second image
cv.imshow("Display 2", img2)

#Window will show until exit key is pressed (Return)
k = cv.waitKey(0)

#Save the file if the s key is pressed
#Ord returns the ASCII value to compare to k because k is also an ASCII value returned by the waitKey function
if k ==ord("s"):
    cv.imwrite("test.png", img)
