'''
Server-side
This is the server tasked with receiving 
image data for predictions.
'''
import socket
import cv2
import numpy
from time import sleep
import time
import csv
# local modules
import getImage
import model
import reportPred

def processing(data):
    path = '/home/raxit/findFire/server/models/model_final.pth'
    cuda = False
    #try:
    predictor = model.loadModel(path, cuda)
    prediction, probability = model.getPred(data, predictor)
    message_sid = -1
    if prediction in ['Fire', 'Smoke'] and probability >= 50:
        now = time.strftime('%d-%m-%Y at %H:%M:%S')
        content = prediction + 'detected on' + now
        recipient = '+918084272322'
        message_sid = reportPred.report(content, recipient)
        print(message_sid)

    with open('preds.csv', 'w', newline = '\n') as file:
        writer = csv.writer(file)
        timestamp = time.strftime(time.strftime('%d%m%Y_%H%M%S'))
        writer.writerow([timestamp, data, prediction, probability, message_sid, '\n' ])
    file.close()

    return 0

    # except :
    #     return 1


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

        status = processing(data)
    
        if status == 0:
            print(status)
        else: 
            print('error')


if __name__ == "__main__":
    getData()