import cv2

#Load the image
img = cv2.imread("C:\\Users\\begin\\PycharmProjects\\panorama\\my_pics\\new_pic.jpg")

#Image Dimensions
height = img.shape[0]
width = img.shape[1]
x = 0
y = 0

#Width and Height of a cropped piece and partial overlap
crop_width = width/4
overlap_sides = 0.50 * (width/4)
crop_height = height/2
overlap_tops = 0.50 * (height/2)

print(f"Total height of the image is: {height}")
print(f"Total width of the image is: {width}")

#Crop into 8 pictures
cropped_left_corner = img[y:int(crop_height + overlap_tops), x:int(crop_width + overlap_sides)]
cropped_middle_left = img[y:int(crop_height + overlap_tops), int(crop_width - overlap_sides): int((2 * crop_width) + overlap_sides)]
cropped_middle_right = img[y:int(crop_height + overlap_tops), int((2 * crop_width) - overlap_sides): int((3 * crop_width) + overlap_sides)]
cropped_right_corner = img[y:int(crop_height + overlap_tops), int((3 * crop_width) - overlap_sides): int(width)]
cropped_bottom_left_corner = img[int(crop_height - overlap_tops):int(height), x:int(crop_width + overlap_sides)]
cropped_bottom_middle_left = img[int(crop_height - overlap_tops): int(height), int(crop_width - overlap_sides): int((2 * crop_width) + overlap_sides)]
cropped_bottom_middle_right = img[int(crop_height - overlap_tops): int(height), int((2 * crop_width) - overlap_sides): int((3 * crop_width) + overlap_sides)]
cropped_lower_right_corner = img[int(crop_height - overlap_tops): int(height), int((3 * crop_width) - overlap_sides): int(width)]

#Save them
cv2.imwrite("my_crops/crop1.jpg", cropped_left_corner)
cv2.imwrite("my_crops/crop2.jpg", cropped_middle_left)
cv2.imwrite("my_crops/crop3.jpg", cropped_middle_right)
cv2.imwrite("my_crops/crop4.jpg", cropped_right_corner)
cv2.imwrite("my_crops/crop5.jpg", cropped_bottom_left_corner)
cv2.imwrite("my_crops/crop6.jpg", cropped_bottom_middle_left)
cv2.imwrite("my_crops/crop7.jpg", cropped_bottom_middle_right)
cv2.imwrite("my_crops/crop8.jpg", cropped_lower_right_corner)


cv2.imshow("Frame1", cropped_left_corner)
cv2.imshow("Frame2", cropped_middle_left)
cv2.imshow("Frame3", cropped_middle_right)
cv2.imshow("Frame4", cropped_right_corner)
cv2.imshow("Frame5", cropped_bottom_left_corner)
cv2.imshow("Frame6", cropped_bottom_middle_left)
cv2.imshow("Frame7", cropped_bottom_middle_right)
cv2.imshow("Frame8", cropped_lower_right_corner)

k = cv2.waitKey(0)

