# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-boilerplate',
    version='0.0.8',
    description='Boilerplate code I keep including in all Django installs.',
    author='Ken Colton',
    author_email='kcolton@gmail.com',
    url='https://github.com/kcolton/django-boilerplate',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
