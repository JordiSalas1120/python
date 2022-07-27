from cv2 import cv2 
import numpy as np #para trabajar numpy se necesita trabajar con matriz

valorgaus=1
valorkernel=33
original=cv2.imread('monedassoles.jpg')
gris=cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(gris,(valorgaus, valorgaus) ,0)
canny=cv2.Canny(gauss, 60, 100)#es una matriz mxm mientras mas el valor, mas amplio es su desenfoque
kernel=np.ones((valorkernel, valorkernel),np.uint8)#trabajar con 8 bites cuando se trabaja con matriz

cierre=cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

contornos, jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("monedas encontradas: {}".format(len(contornos)))
cv2.drawContours(original, contornos, -1, (0,0,255),2)
#MOSTRAR RESULTASDOS
#cv2.imshow("Grises", gris)
#cv2.imshow("gauss", gauss)
#cv2.imshow("Canny", canny)
cv2.imshow("Resultado", original)

cv2.waitKey()