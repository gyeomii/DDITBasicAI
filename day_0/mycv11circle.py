import cv2

img1 = cv2.imread('Lenna.png')
print("img1",img1)

center_coordinates = (280, 300)
radius = 100
color = (255, 0, 0)
thickness = 2
img1_circle = cv2.circle(img1, center_coordinates, radius, color, thickness)



cv2.imshow('img1_circle', img1_circle)
cv2.waitKey(0)
cv2.destroyAllWindows()