import cv2

img_w = cv2.imread('white.png')
img_r = cv2.imread('red.png')

# cv2.imshow('img_w', img_w)
# cv2.imshow('img_r', img_r)

print(img_r.shape)
ii,jj,c= img_r.shape

i_off = 0
j_off = 20

for i in range(ii):
    for j in range(jj):
        img_w[i+i_off][j+j_off][0]=img_r[i][j][0]
        img_w[i+i_off][j+j_off][1]=img_r[i][j][1]
        img_w[i+i_off][j+j_off][2]=img_r[i][j][2]
        
cv2.imshow('img_w', img_w)

cv2.waitKey(0)
cv2.destroyAllWindows()



