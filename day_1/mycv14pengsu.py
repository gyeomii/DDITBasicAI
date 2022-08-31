
import cv2

file = "pengsu.png"
s_img = cv2.imread("h2.png", cv2.IMREAD_COLOR)
x_offset=90
y_offset=160

original = cv2.imread(file, cv2.IMREAD_COLOR)



y1, y2 = y_offset, y_offset + s_img.shape[0]
x1, x2 = x_offset, x_offset + s_img.shape[1]

alpha_s = s_img[:, :, 1] / 255.0
alpha_l = 1.0 - alpha_s

original[y1:y2, x1:x2, 0] = (alpha_s * s_img[:, :, 0] + alpha_l * original[y1:y2, x1:x2, 0])
original[y1:y2, x1:x2, 1] = (alpha_s * s_img[:, :, 1] + alpha_l * original[y1:y2, x1:x2, 1])
original[y1:y2, x1:x2, 2] = (alpha_s * s_img[:, :, 2] + alpha_l * original[y1:y2, x1:x2, 2])

# for c in range(0, 3):
#     original[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] + alpha_l * original[y1:y2, x1:x2, c])



cv2.imshow('Original', original)


cv2.waitKey(0)
cv2.destroyAllWindows()



