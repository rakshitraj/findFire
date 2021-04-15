from os import error
import getImage
import sendImage
import removeImg
import cv2
import time
import sys

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
    int count = 0
    while True:
        status =  process(ip)
        if status == -1:
           print('error')
        else:
            print (status)
        time.sleep(1.5)
        count+=1
        if (count > 1000):
            count = 0
            pass