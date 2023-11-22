# Rieser,Alix , Molchanova, Aleksandra, Lama,Christopher

import os
import subprocess
from imgDiff import diff

username = "picocluster"
cdCmdPreliminary = "cd /home/picocluster/Desktop/research/preliminary;"
cdCmdPostPreliminary = "cd /home/picocluster/Desktop/research/postpreliminary;"
CdResearch = "cd /home/picocluster/Desktop/research;"
# Preliminary image stitching

# call the nodes to commence image stitching through an ssh command
for i in range(1,5):
    subprocess.run(["ssh", f"pc{i}", cdResearch,"python3 stitcher.py", "preliminary", f"pc{i}"])

# --> transfer the files <--
preliminaryLocation = "/home/picocluster/Desktop/research/outPics"
recieveLocationPostpreliminary = "/home/picocluster/Desktop/research/postpreliminary"
receiveLocationHeadNode = "/home/picocluster/Desktop/research/outPics"
# W3 sends T1 to W1
subprocess.run(["ssh", "pc3", cdResearch,"python3 sendImage.py", "pc3", "pc1",preliminaryLocation,username+"@pc1:"+ recieveLocationPostpreliminary])

#W4 sends T1 to W2
subprocess.run(["ssh", "pc4", cdResearch,"python3 sendImage.py", "pc4", "pc2", preliminaryLocation,username+"@pc2:"+ recieveLocationPostpreliminary])

#W1 sends T2 to W3
subprocess.run(["ssh", "pc1", cdResearch,"python3 sendImage.py", "pc1", "pc3", preliminaryLocation,username+"@pc3:"+ recieveLocationPostpreliminary])

#W4 sends T1 to W2
subprocess.run(["ssh", "pc2", cdResearch,"python3 sendImage.py", "pc2", "pc4", preliminaryLocation, username+"@pc4:"+recieveLocationPostpreliminary ])

# combine the images
for i in range(1,5):
    subprocess.run(["ssh", f"pc{i}", cdResearch, "python3 stitcher.py", "postpreliminary", f"pc{i}"])

#send files to head node
for i in range(1,5):
    subprocess.run(["ssh", f"pc{i}",cdResearch, "python3 sendImage.py", f"pc{i}", "pc0", preliminaryLocation, username+"@pc0:"+ receiveLocationHeadNode])

#stitch the files in the head node
subprocess.run(["python3 stitcher.py", "final", "main"])

# calculate image diff
imageList = os.listdir("postpreliminary")
diff(imageList[0],imageList[1], "final")
