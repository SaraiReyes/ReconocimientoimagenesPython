#imagen = cv2.imread('formasgeometricas.png')
import cv2
img = cv2.imread('D:\\Biblioteca\\Escritorio\\python\\ReconocimientoF\\formasgeometricas.png',0)
cv2.imshow('image',img)
k=cv2.waitKey(5000) & 0xFF
cv2.destroyAllWindows()