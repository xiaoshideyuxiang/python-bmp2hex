#!/usr/bin/env python
# -*- encoding=utf-8 -*-

# https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python

# python2 下运行imageio 需要imageio_v2.6.x及以下版本
# https://github.com/imageio/imageio/archive/v2.6.1.zip
# 进行安装：pip install imageio-2.6.1.zip

import imageio

import PIL

# 查找筛选文件，glob, https://blog.csdn.net/qq_27694835/article/details/108646147
import os
import glob

# 使用 imageio 生成gif 有个问题：原图的背景是透明的，得到的gif背景是绿色的
images = []

image_iter = sorted(glob.glob("*.png"), key=os.path.getmtime)
for _file in image_iter:
    print _file
    images.append(imageio.imread(_file))

if len(images) is not 0:
    imageio.mimsave("new.gif", images)
