from os import error
import getImage
import sendImage
import cv2
import time

def process(ip):
    status = -1
    filepath = getImage.recordData()
    
    if filepath:
        try:
            status = sendImage.sendData(filepath, ip)
        except:
            pass
    return status

if __name__ == '__main__':
    ip = sys.argv[1]
    while True:
        status =  process(ip)
        if status == -1:
           print('error')
        else:
            print (status)
        time.sleep(1.5)