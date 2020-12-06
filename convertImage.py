#!/usr/bin/env python

# https://pythontic.com/image-processing/pillow/convert

import PIL

print("hello this is a pillow example")

from PIL import Image
Image.open("coffee-icon64x64.png").save("coffee-icon64x64.bmp")

print(">>>>finish")