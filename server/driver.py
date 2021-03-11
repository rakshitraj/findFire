'''
Server-side
This is the server tasked with receiving 
image data for predictions.
'''
import socket
import cv2
import numpy
from time import sleep
# local modules
import getImage

def getData():
    
    # Host and port
    TCP_HOST = 'localhost'
    TCP_PORT = 5001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_HOST,TCP_PORT))
    s.listen(True)

    while True:

        conn, addr = s.accept()
        data = getImage.getImgData(s, conn)

        # # Code for testing received images
        # decimg=cv2.imdecode(data,1)
        # cv2.imshow('SERVER',decimg)
        # #cv2.waitKey(0)
        # sleep(5)
        # cv2.destroyAllWindows()

if __name__ == "__main__":
    data = getData()