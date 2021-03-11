from os import error
import getImage
import sendImage
import cv2

def process():
    status = -1
    filepath = getImage.recordData()
    
    if filepath:
        status = sendImage.sendData(filepath)
    return status

if __name__ == '__main__':
        status =  process()
        if status == -1:
           print('error')
        else:
            print (status)