"""TIFF image reader.
Reads TIFF image data and saves it to a file.

Recipe from http://stackoverflow.com/a/7572079/4143531.

Maksim Rakitin, 2016.
"""

import numpy as np
from PIL import Image

img_file = 'data/33ecb55e-7d0b-4077-95e2_000003.tiff'

im = Image.open(img_file)

imarray = np.array(im)

print('imarray.shape: {}  im.size: {}'.format(imarray.shape, im.size))

# idxs_more = np.where(imarray >= imarray.max(0.5))
idxs_less = np.where(imarray < imarray.max()*0.02)
imarray[idxs_less] = np.uint16(0)

im = Image.fromarray(imarray)

im.show()
