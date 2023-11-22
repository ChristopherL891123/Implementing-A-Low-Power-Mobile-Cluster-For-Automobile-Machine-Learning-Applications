import os
import sys
import subprocess

def delete():
    
    # this script takes in one argument:
        # 1. The folder whose contents to delete ( not the folder itself)
        
    cd = "cd" + sys.argv[1]
    subprocess.run([cd])    
    subprocess.run(["rm", "*.jpg" ])
delete()