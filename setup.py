"""Setup script for mytool."""

from setuptools import setup


def readme():
    """Make description from repo README.md."""
    with open('README.md') as f:
        return f.read()


setup(
    name='mytools',
    version='2017.2.21a',
    description='Collection of commonly re-used python functons and classes.',
    long_description=readme(),
    classifiers=[
        'License :: Public Domain',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 3.5'
        'Topic :: Utilities',
    ],
    url='http://github.com/cgiacofei/python-tools',
    author='Chris Giacofei',
    author_email='',
    license='http://unlicense.org/UNLICENSE',
    packages=['nested_dict'],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)

