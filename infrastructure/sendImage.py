# Rieser,Alix , Molchanova, Aleksandra, Lama,Christopher
import os
import sys
import subprocess
import traceback as t

# this script accepts two parameters:
    # 1. The node that is sending the image
    # 2. The node that is recieving the image
    # 3. The relative address of the image in the sender
    # 4. The username@pi: along with the absolute address to store the image
    # 5. The directory to scp.

# the command: scp /path/to/file username@a:/path/to/destination
def sendFiles():
    try:
        log = open("log.txt", 'w')
        log.write("> ")

        sender = sys.argv[1]
        reciever = sys.argv[2]
        senderImgAddr = sys.argv[3]
        recieverImgAddr = sys.argv[4]
        folderToScp = sys.argv[5]
        fileList = [image for image in os.listdir(folderToScp)]
	# SCP ENTIRE DIRECTORY HERE
        send = subprocess.run(["ssh",sender,";","scp","-r", senderImgAddr, recieverImgAddr])
        log.write("FILE SENT")
        
        
        
        log.close()
        
    except:
        log.write(t.print_exc())
        log.close()

sendFiles()

