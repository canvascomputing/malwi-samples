"""Utils for image operations."""
import cv2
import itertools
import numpy as np

def bytes_to_img(data):
    """Converts bytes to image."""

    nparr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def padding(img, shape, bg=255):
    """Padding image to match 'shape'."""

    if len(img.shape) == 3:
        shape = [shape[0], shape[1], img.shape[2]]
    res = np.ones(shape, dtype='uint8') * bg

    x = shape[0] - img.shape[0]
    y = shape[1] - img.shape[1]
    assert x >= 0 and y >= 0, (
        'shape {} is smaller than board shape {}'.format(img.shape, shape))
    hx, hy = x >> 1, y >> 1
    res[hx:hx+img.shape[0], hy:hy+img.shape[1]] = img
    return res

def concat(img_list, rows, cols):
    """Concatnates a series of images into size (rows, cols)."""

    assert len(img_list) == rows * cols, (
        'size of list {} should be equal to {} * {}'.format(
            len(img_list), rows, cols))

    for img in img_list[1:]:
        assert img.shape == img_list[0].shape, (
            'shape not match {} != {}'.format(img.shape, img_list[0].shape))

    img = np.concatenate([
        np.concatenate(img_list[i*cols: (i+1)*cols], axis=1)
        for i in range(rows)], axis=0)

    return img

def split(img, rows, cols):
    """Splits a large image into rows * cols blocks."""

    x = img.shape[0] // rows
    y = img.shape[1] // cols
    return [img[sx: sx + x, sy: sy + y]
            for sx in range(0, img.shape[0], x)
            for sy in range(0, img.shape[1], y)]

def __test():
    img = np.random.randint(0, 256, size=(256, 256, 3))
    imgs = split(img, 16, 16)
    rec = concat(imgs, 16, 16)
    assert (img == rec).all()
    print('success')


if __name__ == '__main__':
    __test()
