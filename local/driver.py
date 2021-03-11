import getImage
import sendImage
import cv2

def process():
    filename = getImage.recordData()
    check, frame = cv2.imread(filename)

    if check:
        sendImage.sendData(frame)
    else: 
        return -1

if __name__ == '__main__':
    while True:
        process