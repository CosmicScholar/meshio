# -*- coding: utf-8 -*-
#
import codecs
import os

from setuptools import setup, find_packages

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, 'meshio', '__about__.py'), 'rb') as f:
    # pylint: disable=exec-used
    exec(f.read(), about)


def read(fname):
    return codecs.open(os.path.join(base_dir, fname), encoding='utf-8').read()


setup(
    name='meshio',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=find_packages(),
    description='I/O for various mesh formats',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/nschloe/meshio',
    project_urls={
        'Issues': 'https://github.com/nschloe/meshio/issues',
        },
    license=about['__license__'],
    platforms='any',
    install_requires=[
        'numpy',
        'pipdate',
        ],
    extras_require={
        'all': ['netCDF4', 'h5py'],
        'exodus': ['netCDF4'],
        'hdf5': ['h5py'],  # MED, MOAB, XDMF formats
        },
    scripts=[
        'tools/meshio-convert',
        ],
    classifiers=[
        about['__status__'],
        about['__license__'],
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering'
        ]
    )
