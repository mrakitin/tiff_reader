"""TIFF image reader.
Reads TIFF image data and saves it to a file.

Recipe from http://stackoverflow.com/a/7572079/4143531.

Maksim Rakitin, 2016.
"""

import numpy as np
from PIL import Image

# img_file = 'data/33ecb55e-7d0b-4077-95e2_000003.tiff'
img_file = 'data/xf21id1_cam01_H5_V5_029.tif'

im = Image.open(img_file)
# im.show()
imarray = np.log(np.array(im))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


print('imarray.shape: {}  im.size: {}'.format(imarray.shape, im.size))
# max_value = imarray.max() * 0.25
# imarray += np.uint16(imarray.max()*0.05)

# idxs_more = np.where(imarray >= imarray.max(0.5))
idxs_less = np.where(imarray < 0.0)  # max_value)
imarray[idxs_less] = np.uint16(0)

im = Image.fromarray(imarray)

im.show()
