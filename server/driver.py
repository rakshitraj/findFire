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
import sys
import os
import getpass
# local modules
import getImage
import model
import reportPred

def _show(data):
    # Code for testing received images
        decimg=cv2.imdecode(data,1)
        cv2.imshow('SERVER',decimg)
        #cv2.waitKey(0)
        sleep(5)
        cv2.destroyAllWindows()

def processing(data, recipient, predictor):
    
    try:
        prediction, probability = model.getPred(data, predictor)
        message_sid = -1
        if prediction in ['Fire', 'Smoke'] and probability >= 50:
            now = time.strftime('%d-%m-%Y at %H:%M:%S')
            content = prediction + ' detected on ' + now
            message_sid = reportPred.report(content, recipient)
            print(message_sid)

        predsPath = os.path.join('/home', getpass.getuser(), 'findFire/server/preds.csv')
        with open(path= predsPath, 'a', newline = '\n') as file:
            writer = csv.writer(file)
            timestamp = time.strftime(time.strftime('%d%m%Y_%H%M%S'))
            writer.writerow([timestamp, data, prediction, probability, message_sid, '\n' ])
        file.close()

        return 0

    except :
        print(sys.exc_info()[0])
        return 1


def getData(ip, recipient, predictor):
    
    # Host and port
    TCP_HOST = ip
    TCP_PORT = 10001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_HOST,TCP_PORT))
    s.listen(True)

    while True:

        conn, addr = s.accept()
        data = getImage.getImgData(s, conn)

        # Show image for testing, time ~ 5 seconds
        # _show(data)

        status = processing(data, recipient, predictor)
    
        if status == 0:
            print(status)
        else: 
            print('error')


if __name__ == "__main__":
    ip = sys.argv[1]        # IP address of Server
    recipient = sys.argv[2] # Phone number of Recipient
    # Load model
    path = os.path.join('/home', getpass.getuser(), 'findFire/server/models/model_final.pth')
    cuda = False
    predictor = model.loadModel(path, cuda)
    # Listen for incoming images
    getData(ip, recipient, predictor)