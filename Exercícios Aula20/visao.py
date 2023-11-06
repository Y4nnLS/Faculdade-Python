import cv2
import matplotlib.pyplot as plt

img = cv2.imread("ronchi_sp.bmp", cv2.IMREAD_GRAYSCALE)

# altura, largura = img.shape

# for i in range(altura):
#     for j in range(largura):
#         img[i, j] = img[i, j] * 1

img_out = cv2.medianBlur(img, 5)
cv2.imwrite('img_out.bmp', img_out)

img = cv2.equalizeHist(img)

hist = cv2.calcHist([img], [0], None, [256], [0,256])

plt.plot(hist)
plt.show()

cv2.imshow('Imagem', img)
cv2.waitKey(0)
cv2.destroyAllWindows()