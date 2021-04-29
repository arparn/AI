import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

if __name__ == '__main__':

    X = np.genfromtxt("happysadpixels.csv", delimiter=",", dtype=int)
    y = np.genfromtxt("happysadlabels.csv", delimiter=",", dtype=int)

    X.shape
    y.shape

    plt.imshow(X[0].reshape(6, 6))

    nn = MLPClassifier(hidden_layer_sizes=(3,), max_iter=2000)

    nn = nn.fit(X, y)
    print("Iterations", nn.n_iter_, "Final loss", nn.loss_)

    my_weights1 = []
    my_weights2 = []
    my_weights3 = []

    for i in range(36):
        my_weights1.append(nn.coefs_[0][i][0])
        my_weights2.append(nn.coefs_[0][i][1])
        my_weights3.append(nn.coefs_[0][i][2])
    plt.imshow(np.array(my_weights1).reshape(6, 6))
    plt.show()
    plt.imshow(np.array(my_weights2).reshape(6, 6))
    plt.show()
    plt.imshow(np.array(my_weights3).reshape(6, 6))
    plt.show()

    out_weights1 = []
    out_weights2 = []

    for j in range(3):
        out_weights1.append(nn.coefs_[1][j][0])
        out_weights2.append(nn.coefs_[1][j][1])

    plt.imshow(np.array(out_weights1).reshape(3, 1))
    plt.show()
    plt.imshow(np.array(out_weights2).reshape(3, 1))
    plt.show()


