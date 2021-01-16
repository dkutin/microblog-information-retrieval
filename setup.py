from distutils.core import setup

from setuptools import find_packages, setup
from setuptools.command.install import install as _install
from setuptools.command.develop import develop as _develop

requirements = [

]

setup(name='microblog-information-retrieval-system',
        version='0.0.1',
        author='Dmitry Kutin',
        author_email='dkuti025@uottawa.ca',
        license="MIT",
        # install_requirements=requirements,
        url='https://github.com/dkutin/csi4107-assignment1',
        description='CSI 4107 Assignment 1, a microblog information retrieval system.',
        long_description=open('README.md').read()
)