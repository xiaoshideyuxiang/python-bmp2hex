#!/usr/bin/env python

# https://pythontic.com/image-processing/pillow/extract%20frames%20from%20animated%20gif

from PIL import Image

from PIL import GifImagePlugin

obj = Image.open("./TinyImaginaryAvocet-size_restricted.gif")

print(obj.is_animated)
print(obj.n_frames)


for i in range(obj.n_frames):
    obj.seek(i)
    _name = "./"
    _name += str(i)
    _name += ".png"
    obj.save(_name)
