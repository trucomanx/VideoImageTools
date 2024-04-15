#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name   ='VideoImageTools',
    version='0.1.0',
    author='Fernando Pujaico Rivera',
    author_email='fernando.pujaico.rivera@gmail.com',
    packages=['VideoImageTools'],
    #scripts=['bin/script1','bin/script2'],
    url='https://github.com/trucomanx/VideoImageTools',
    license='GPLv3',
    description='Tools to work with image and video processing',
    #long_description=open('README.txt').read(),
    install_requires=[
       "numpy", #"Django >= 1.1.1",
       "Pillow", #
       "opencv-python"
    ],
)

#! python setup.py sdist bdist_wheel
# Upload to PyPi
# or 
#! pip3 install dist/VideoImageTools-0.1.tar.gz 
