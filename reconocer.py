#    recoocer figuras geometricas
# pip install opencv-python
import cv2
import numpy as np
image = cv2.imread('D:\\Biblioteca\\Escritorio\\python\\ReconocimientoF\\formasgeometricas.png')

try:
    cv2.imshow('result', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except:
    print("Here")