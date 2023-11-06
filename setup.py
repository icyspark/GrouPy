# @Time: 2023/10/27 14:13
# @Author: Feite Zheng
#!/usr/bin/env python

from distutils.core import setup

setup(
    name='GrouPy',
    version='0.1.2',
    description='Group equivariant convolutional neural networks',
    author='Taco S. Cohen',
    author_email='taco.cohen@gmail.com',
    packages=['groupy', 'groupy.garray', 'groupy.gconv', 'groupy.gconv.pytorch_gconv', 'groupy.gfunc', 'groupy.gfunc.plot'],
)
