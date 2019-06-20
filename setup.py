#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/appleimporter.svg
        :target: https://pypi.python.org/pypi/appleimporter
.. image:: https://img.shields.io/travis/sampathP/appleimporter.svg
        :target: https://travis-ci.org/sampathP/appleimporter

Image, video import tool for apple devices


Links:
---------
* `Github <https://github.com/sampathP/appleimporter>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Sampath Priyankara",
    author_email='sam47priya@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Image, video import tool for apple devices",
    entry_points={
        'console_scripts': [
            'appleimporter=appleimporter.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=__doc__,
    include_package_data=True,
    keywords='appleimporter',
    name='appleimporter',
    packages=find_packages(include=['appleimporter']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sampathP/appleimporter',
    version='0.1.0',
    zip_safe=False,
)
