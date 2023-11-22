import imgDiff
import stitcher

images = [cv2.imread(image_path) for image_path in image_paths if image_path.endswith(imageFormat)]
        
stitcher = cv2.Stitcher.create()

(status, stitched) = stitcher.stitch(images)

cv2.imwrite(outputFilename, stitched)