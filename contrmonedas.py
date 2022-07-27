from cv2 import cv2 
import numpy as np

def ordenarpuntos(puntos):
    n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()#esta creando una matriz.
    y_order = sorted(n_puntos, key=lambda n_puntos:n_puntos[1])#ordenamos la matriz ya que python lo resulve desordenado inicia a recorrer desde 0 pero se pone 1 ya que se resta 1. recorre solo 0 ya que sera el centro. pero para ser recorrido debecolocarse "0:1"
    x1_order = y_order[:2]#recorrera desde el cero hasta el 1
    x1_order = sorted(x1_order, key=lambda x1_order:x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order:x1_order[0])


    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

def alineamiento(imagen, ancho, alto):
    imagenalineada = None
    grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, umbral = cv2.threshold(grises, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("Umbral", umbral)
    contorno= cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contorno = sorted(contorno, key=cv2.contourArea, reverse = True)[:1]#mas que todo para las x. iniciara del mator al menor, por ese el reverse
    for c in contorno:
        epsilon=0.01*cv2.arcLength(c, True)#recorre los contornos
        approximacion = cv2.approxPolyDP(c, epsilon, True)#hace una aproximacion de contornos
        if len(approximacion)==4:#len es para contar una lista
            puntos = ordenarpuntos(approximacion)
            puntos1=np.float32(puntos)#convierte los puntos en enteros normales
            puntos2=np.float32([[0,0], [ancho, 0], [0, alto], [ancho, alto]]) #(x,y) de la matriz que se crea
            M = cv2.getPerspectiveTransform(puntos1, puntos2)
            imagenalineada = cv2.warpPerspective(imagen, M, (ancho, alto))
    return imagenalineada
capturevideo = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    tipocamara, camara=capturevideo.read()
    if tipocamara==False:
       break
    imagenA6 = alineamiento(camara, ancho=480, alto=677)
    if imagenA6 is None: #si hay imagen
        puntos=[]
        imagengris=cv2.cvtColor(imagenA6,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(imagengris,(5,5), 1)
        _, umbral2=cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)# se usa 2 cv2 por que es video. esta configurado para que se en papel blanco
        cv2.imshow("Umbral",umbral2)
        contorno2=cv2.findContours(umbral2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagenA6, contorno2, -1, (255,0,0),2)
        suma1=0.0
        suma2=0.0
        suma3=0.0
        for c2 in contorno2:
            area=cv2.contourArea(c2)
            momentos = cv2.moments(c2)
            if (momentos["m00"]):
                momentos["m00"]-1.0
            x=int(momentos["m10"]/momentos["m00"])
            y=int(momentos["m01"]/momentos["m00"])

            if area<14948 and area>14000:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagenA6, "bs/ 2", (x,y), font, 0,75, (0,255,0), 2)
                suma1=suma1+2
            
            if area<12800 and area>10900:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagenA6, "bs/ 1", (x,y), font, 0,75, (0,255,0), 2)
                suma2=suma1+1
            
            if area<10000 and area>8900:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagenA6, "bs/ 0.50", (x,y), font, 0,75, (0,255,0), 2)
                suma3=suma1+0.5
        total = suma1+suma2+suma3
        print("Sumatoria tortal en monedas:",round(total,2))#round dice que numeros mostrara y con cuantos decimales
        cv2.imshow("Imagen A6", imagenA6)
        cv2.imshow("CAMARA", camara)
    if cv2.waitKey(1) == ord ('q'):
        break
capturevideo.release()#detiene la captura del video
cv2.destroyAllWindows()