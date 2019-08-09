#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
setup file for the test package
"""

from setuptools import setup, find_packages

with open('requirements.txt') as stream:
    REQUIREMENTS = stream.read().splitlines()

setup(
    name='longtask',
    version='1.0.0',
    description="A test case of long running task",
    author="Giuseppe Broccolo",
    author_email='g.broccolo.7@gmail.com',
    packages=find_packages(),
    package_dir={
        'longtask': 'longtask',
    },
    entry_points={
        'console_scripts': [
            'longtask=longtask.longtask:add',
        ]
    },
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False,
    keywords='longtask',
    classifiers=[],
)
