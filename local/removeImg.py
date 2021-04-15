import os
import sys
import glob
import getpass

def remove1000():
    
    path = os.path.join('/home', getpass.getuser(), 'findFire/local/raw/*.jpg')
    files = glob.glob(path)
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


if __name__ == '__main__':
    path = os.path.join('/home', getpass.getuser(), 'findFire/local/raw/*.jpg')
    files = glob.glob(path)
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))