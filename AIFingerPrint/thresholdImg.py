import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('./originImg/jjae.png',0)

blur = cv2.GaussianBlur(img,(5,5),0)

ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

resize = cv2.resize(th3, (300,200))
rotate = cv2.rotate(resize, cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.imwrite('./resizeImg/jjae.png', rotate)