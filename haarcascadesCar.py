import cv2
import numpy as np

video = cv2.VideoCapture("4.Geçit Stream 1.2.mp4")

carsFound = cv2.CascadeClassifier("cars.xml")

while True:
    ret,kare = video.read()

    gray = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    cars = carsFound.detectMultiScale(gray, 1.1, 3) 

    for (x,y,w,h) in cars:
            cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),3)


    cv2.imshow("arabalar",kare)

    if cv2.waitKey(5) & 0xFF ==ord('q'):
        break

video.release()
cv2.destroyAllWindows()    

