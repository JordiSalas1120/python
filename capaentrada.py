import cv2 as cv
import numpy as np 
camara = cv.VideoCapture(0)#abrir camara

ruidos = cv.CascadeClassifier('C:/Users/Jordi/Desktop/Curso de python/proyectos_ia/reconocimientofacial/haarcascade_frontalface_default.xml')
while True:
    _,captura=camara.read()#captura  de la camara
    grises=cv.cvtColor(captura, cv.COLOR_BGR2GRAY)
    cara=ruidos.detectMultiScale(grises, 1.3, 5)#reconocimiento de caras. el 1 significa el 100 por ciento. 1.5 seria el 50 por ciento
    
    for (x,y,e1,e2) in cara:#recorre todos los puntos de lcara
        cv.rectangle(captura, (x,y), (x+e1,y+e2),(0, 255, 0),2)
    cv.imshow("Resultado Rostro", captura)

    if cv.waitKey(1) == ord('q'):
        break
    
    camara.release()#release destruye vualquier vemtama abierta
    cv.destroyAllWindows()    