"""
打包成图片
"""
import os

from PIL import Image
import numpy as np


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def packimg(array, i, file_path):
    data = list(chunks(array, 28))
    data = np.array(data)
    data = np.matrix(data)
    img = Image.fromarray(data.astype(np.uint8))
    img.save(file_path + '/' + str(i) + '.jpg', 'JPEG')
    return 0

