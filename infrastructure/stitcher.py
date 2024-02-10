# Rieser,Alix , Molchanova, Aleksandra, Lama,Christopher
import os

import cv2
from datetime import datetime
import traceback as t
import sys

# this script takes in two arguments:
    # 1. stage or mode of stitching, either preliminary or postpreliminary, final is meant only to be used on the head node.
	#preliminary saves the output picture to the outPics directory,to be sent to another node's postpreliminary directory.
    # 2. the node that will do the stitiching.


def stitch():
    
    try:
        log = open("log.txt",'w')
        log.write("> ")
        
        imageFormat = ".jpg"  # Specify the image format you want to save
        node = sys.argv[2]
        outputFilename = node + "_" + str(datetime.now()).replace(" ", "_").replace("-","_").replace(":","_")

        if sys.argv[1] == "preliminary":
            mode = "preliminary" # before: outPics
            image_paths = os.listdir("preliminary") # preliminary has the raw images

        if sys.argv[1] == "postpreliminary":
            mode = "outPics" # write to that folder
            image_paths = os.listdir("postpreliminary") # 
        else: # it is final
            mode = "final"
            image_paths = os.listdir("outPics") # only in head node

        if mode == "preliminary":
            filePrefix = "r1"
        elif mode == "postpreliminary":
            filePrefix == "r2"
        
        imagesRound1 = [cv2.imread(image) for image in image_paths if image.endswith("T1")]
        imagesRound2 = [cv2.imread(image) for image in image_paths if image.endswith("T2")]

        stitcher = cv2.Stitcher.create()

        (status, stitched) = stitcher.stitch(imagesRound1)
        
        cv2.imwrite(f"{mode}/" + filePrefix+outputFilename+"_T1"+imageFormat, stitched)
        log.write(f"image written to {mode} in {node}")

        (status, stitched) = stitcher.stitch(imagesRound2)
        cv2.imwrite(f"{mode}/" + filePrefix + outputFilename+"_T2" + imageFormat, stitched)

        log.write(f"image written to {mode} in {node}")
        log.close()
        
    except:
        
        log.write(t.print_exc())
        log.close()

stitch()
