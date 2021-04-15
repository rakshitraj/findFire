import socket
import cv2
import numpy
import sys

def sendData(filepath, host: str):
    frame = cv2.imread(filename=filepath)

    if frame is not None:
        TCP_IP = host
        TCP_PORT = 10001

        sock = socket.socket()
        sock.connect((TCP_IP, TCP_PORT))

        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = numpy.array(imgencode)
        stringData = data.tostring()

        sock.sendto(str(len(stringData)).ljust(16).encode(), (TCP_IP, TCP_PORT))
        sock.send(stringData)
        sock.close()

        return 0    # successful completion of task
    return -1   # task unsuccesful


if __name__ == '__main__':
    status = sendData()
