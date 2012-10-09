import numpy as np
from matplotlib import pyplot as plt

from skimage import data, img_as_float
from skimage.feature import harris


def plot_harris_points(image, filtered_coords):
    plt.imshow(image)
    y, x = np.transpose(filtered_coords)
    plt.plot(x, y, 'b.')
    plt.axis('off')

# resultados
plt.figure(figsize=(8, 3))
image = img_as_float(data.load("c.jpeg"))

filtered_coords = harris(image, min_distance=4)

plt.axes([0.2, 0, 0.77, 1])
plot_harris_points(image, filtered_coords)

plt.show()
