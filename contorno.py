from cv2 import cv2 
imagen = cv2.imread('C:/Users/Jordi/Desktop/Curso de python/proyectos_ia/Opencv2/contorno.jpg')#cargamos imagen
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)#llevamos la imagen a escala de grises
_,umbral = cv2.threshold(grises,100, 255, cv2.THRESH_BINARY)#para umbralizar
contorno, jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contorno, -1,(0, 121, 52),3 )

#mostrar
cv2.imshow('Esta es la imagen original', imagen)#mostramos imagen en pantalla
#cv2.imshow('Esta es la imagen en grises', grises)#
cv2.imshow('Umbral', umbral)

cv2.waitKey(0)#con este comando le decimos a python qie espere y no cierre la ventana
cv2.destroyAllWindows()#destruye todas las ventanas

