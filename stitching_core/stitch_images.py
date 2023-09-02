import cv2


# <---> TODO: Incorporate Alix's code for more features. This is just a program that stitches crops of a panoramic image. <--->


image_paths = ['crop1.jpg', 'crop2.jpg', 'crop3.jpg', 'crop4.jpg', 'crop5.jpg', 'crop6.jpg', 'crop7.jpg', 'crop8.jpg']

# load the images
images = [cv2.imread(image_path) for image_path in image_paths]


stitcher = cv2.Stitcher.create()

# stitching
(status, stitched) = stitcher.stitch(images)
cv2.imshow('Stitched Image', stitched)
cv2.waitKey(0)

