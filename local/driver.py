from os import error
import getImage
import sendImage
import cv2
import time

def process():
    status = -1
    filepath = getImage.recordData()
    
    if filepath:
        try:
            status = sendImage.sendData(filepath)
        except:
            pass
    return status

if __name__ == '__main__':
    while True:
        status =  process()
        if status == -1:
           print('error')
        else:
            print (status)
        time.sleep(1.5)