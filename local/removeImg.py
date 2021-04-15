import os
import sys
import glob

def remove1000():
    
    files = glob.glob(os.path.join(os.path.realpath(sys.argv[0], 'local/raw/*.jpg')))
    for f in files:
        try:
            f.unlink()
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


if __name__ == '__main__':
    files = glob.glob('/home/raxit/findFire/local/raw/*.jpg')#os.path.join(os.path.realpath(sys.argv[0]), 'local/raw/*.jpg'))
    for f in files:
        try:
            f.unlink()
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))