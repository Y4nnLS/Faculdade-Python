from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import tree, metrics, svm, linear_model
import cv2
import numpy as np

mnist = datasets.load_digits()
# print(mnist.images[0])
# print(mnist.target[0])

# plota as primeiras 10 imagens do MNIST
# for i in range(10):
#     plt.imshow(mnist.images[i], cmap = plt.cm.gray)
#     plt.show()

# converte o dataset MNIST para o par x e y a serem usados pelo classificador
n_samples = len(mnist.images)
X = mnist.images.reshape((n_samples, -1))
y = mnist.target


# cria um modelo baseado em uma árvore de decisão
# model = tree.DecisionTreeClassifier()
# model = svm.SVC(gamma = 0.001)
model = linear_model.SGDClassifier(loss='hinge', penalty='l2', max_iter=5)

# treina o modelo
model.fit(X, y)

y_pred = model.predict(X)

acc = metrics.accuracy_score(y, y_pred) * 100.0
print(acc)

# carrega a imagem de teste
img = cv2.imread('4.png', cv2.IMREAD_GRAYSCALE)

# redimensiona a imagem para ficar 8x8 com 8x8 pixels
img = cv2.resize(img, (8,8), interpolation=cv2.INTER_AREA)

# inverte as cores da imagem
img = cv2.bitwise_not(img)
img = (img / 255.0) * 16.0
img = img.astype(np.uint8)

img = img.flatten()
print(img)

y_pred = model.predict([ img ])
print(y_pred)

# plt.imshow(img, cmap = plt.cm.gray)
# plt.show()