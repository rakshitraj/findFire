import time
import os.path
from picamera import PiCamera
import getpass

def recordData() :
    # Instantiate PiCamera object
    camera = PiCamera()
    # Generate Filename
    now = time.strftime('%d-%m-%Y %H%M%S')
    filename = now+'.jpg'
    path = os.path.join('/home', getpass.getuser() ,'findFire/local/raw')
    # Image path
    image = os.path.join(path, filename)
    # Capture Image
    camera.capture(image)
    # Return file-path
    return image

if __name__ == '__main__':
    filename = recordData()