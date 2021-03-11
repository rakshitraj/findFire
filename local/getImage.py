import cv2
import time
import os.path

def recordData() :
    key = cv2.waitKey(1)
    camera = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = camera.read()
            
            # # Encoding to JPEG
            # success, buffer = cv2.imencode(".jpg", frame)
            
            ## System Checks
            # print(check)
            #
            # print(frame) # matrix value of images
            # cv2.imshow("Capturing", frame)

            # Save images
            now = time.strftime('%d-%m-%Y %H%M%S')
            filename = now+'.jpg'
            path = '/home/raxit/findFire/local/raw'
            cv2.imwrite(filename=os.path.join(path, filename), img=frame)
            camera.release()
            break
        except:
            # Turn off camera
            camera.release()
