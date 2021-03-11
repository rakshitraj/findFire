'''
Server-side
This is the server tasked with receiving 
image data for predictions.
'''
import socket
import cv2
import numpy

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def getImgData(s, conn):
    try:
        length = recvall(conn,16)
        stringData = recvall(conn, int(length))
        data = numpy.frombuffer(stringData, dtype='uint8')
    finally:
        conn.close()

    # # Code for testing received images
    # decimg=cv2.imdecode(data,1)
    # cv2.imshow('SERVER',decimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return data

if __name__ == "__main__":
    data = getData()