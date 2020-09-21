# Display first 15 images of moles, and how they are classified

import matplotlib.pyplot as plt
import numpy as np

w = 60
h = 40
fig = plt.figure(figsize=(15, 15))
columns = 4
rows = 3


def display_image(Y_train, x_train):
    for i in range(1, columns * rows + 1):
        ax = fig.add_subplot(rows, columns, i)
        if np.argmax(Y_train[i]) == 0:
            ax.title.set_text('Benign')
        else:
            ax.title.set_text('Malignant')
        plt.imshow(x_train[i], interpolation='nearest')
    plt.show()
