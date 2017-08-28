#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexey Sintsov'

from setuptools import setup, find_packages

setup(
    name='CANToolz',
    version='3.6.1',
    description='Framework for black-box Controller Area Network (CAN) bus analysis.',
    author='Alexey Sintsov',
    author_email='alex.sintsov@gmail.com',
    license='Apache 2.0',
    keywords='framework black-box CAN analysis security',
    packages=find_packages(),
    scripts=['bin/cantoolz'],
    url='https://github.com/CANToolz/CANToolz',
    install_requires=[
        'flask',
        'pyserial',
        'mido',
        'numpy',
        'bitstring'
    ],
)
