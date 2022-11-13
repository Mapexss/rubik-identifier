import requests
import numpy as np
import cv2
from colorFilter import color
from scaleImage import imageScale
#from imageFilter import filters

url = "http://192.168.0.102:8080/photo.jpg"
#cap = cv2.VideoCapture(100)
aux = (50, 50)

# index = 0
# arr = []
# while True:
#     cap = cv2.VideoCapture(index)
#     if not cap.read()[0]:
#         break
#     else:
#         arr.append(index)
#     cap.release()
#     index += 1
# return arr
# class main:
#     def applyFilters(self, )
while True:
    image_resp = requests.get(url)
    image_array = np.array(bytearray(image_resp.content), dtype = np.uint8)
    image = cv2.imdecode(image_array, -1)

    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    i = color()
    colorFiltered = i.green(hsv = hsv) #mudar cor do filtro
    
    color = cv2.bitwise_and(blurred, image, mask = colorFiltered) # mostra imagem com cor
    
    contorno, _ = cv2.findContours(colorFiltered, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # contorno (comentar variavel colorFiltered)
    
    for contornos in contorno:
        area = cv2.contourArea(contornos)
        if area > 15000: 
            cv2.drawContours(image, contornos, -1, (255,255,255), 3)
    
    
    
    resized = imageScale.changeScale(aux, True, image, color)
    filtered = imageScale.changeScale(aux, False, image, color)
    
    cv2.imshow("Frame", resized)
    cv2.imshow("Mask", filtered)
    
    
    key = cv2.waitKey(1)
    if key == 27:
        break