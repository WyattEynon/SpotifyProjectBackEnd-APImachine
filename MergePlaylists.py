import sys
import os

if len(sys.argv) == 2:
    print("Merging: "+sys.argv[1])
    dirList=os.listdir()
    for vari in sys.argv[1]:
        if vari in dirList:
            pass
        else:
            raise ValueError('File(s) does/do not exist')
    
        

else:
    print("not enough arguments passed. Requires both csv names before proceeding")