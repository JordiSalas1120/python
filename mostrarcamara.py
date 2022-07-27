import cv2 as cv 
capturarvideo=cv.VideoCapture(0)#abre camara conectada a la pc
if not capturarvideo.isOpened():
    print("no se encontro la camara")
    exit()
while True:
    _,camara=capturarvideo.read()#inicializamos camara. debuelve dos valores por eso el "_"
    grises=cv.cvtColor(camara, cv.COLOR_BGR2GRAY)
    cv.imshow("en vivo",grises)
    if cv.waitKey(1)==ord("q"):#para que no sea infinito, cerramos con la "q"
        break
capturarvideo.release()#destruimos el video
cv.destroyAllWindows()