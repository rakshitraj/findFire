'''
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

def getData():
    
    # Host and port
    TCP_HOST = 'localhost'
    TCP_PORT = 5001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_HOST,TCP_PORT))
    s.listen(True)
    conn, addr = s.accept()

    length = recvall(conn,16)
    stringData = recvall(conn, int(length))
    data = numpy.frombuffer(stringData, dtype='uint8')
    s.close()

    # # Code for testing received images
    # decimg=cv2.imdecode(data,1)
    # cv2.imshow('SERVER',decimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return data

if __name__ == "__main__":
    data = getData()