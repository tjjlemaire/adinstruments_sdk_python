# -*- coding: utf-8 -*-
# @Author: Theo Lemaire
# @Email: theo.lemaire@epfl.ch
# @Date:   2017-06-13 09:40:02
# @Last Modified by:   Theo Lemaire
# @Last Modified time: 2021-05-04 14:05:03

from setuptools import setup

readme_file = 'README.md'


def readme():
    with open(readme_file, encoding="utf8") as f:
        return f.read()


setup(
    name='adi',
    version='1.0',
    description='ADInstruments SDK for Python',
    long_description=readme(),
    url='https://github.com/JimHokanson/adinstruments_sdk_python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    keywords=('ADInstruments SDK Python'),
    author='Jim Hokanson',
    packages=['adi'],
    zip_safe=False
)
