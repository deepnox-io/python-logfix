#!/usr/bin/env python3

""" This file is a part of [python-log-repair](https://github.com/deepnox-io/python-log-repair): script to install Python package.

A Python library to repair an invalid log file, especially logs file of Java application server.

> MIT License
> 
> Copyright (c) 2021 Deepnox
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
> 
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

"""

from setuptools import setup, find_packages
from setuptools.command.egg_info import egg_info


class egg_info_ex(egg_info):
    """ Includes license file into `.egg-info` folder.

    :ref: https://stackoverflow.com/a/66443941
    """

    def run(self):
        # don't duplicate license into `.egg-info` when building a distribution
        if not self.distribution.have_run.get('install', True):
            # `install` command is in progress, copy license
            self.mkpath(self.egg_info)
            self.copy_file('LICENSE', self.egg_info)

        egg_info.run(self)


setup(
    name='log-repair',
    version='0.0.1',
    author='Deepnox',
    author_email='opensource@deepnox.io',
    packages=find_packages(include=['log_repair']),
    package_dir={'': 'src'},
    url='http://pypi.python.org/pypi/log-repair/',
    license='MIT',
    cmdclass={'egg_info': egg_info_ex},
    license_files=('LICENSE',),
    description='A Python library to repair an invalid log file, especially logs file of Java application server.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Logging',
    ],
    test_suite='tests',
    project_urls={
        # 'Documentation': 'https://requests.readthedocs.io',
        'Source': 'https://github.com/deepnox-io/python-log-repair',
    },
)
