from ensurepip import version
from setuptools import setup, find_packages
import os

HERE = os.path.dirname(os.path.realpath(__file__))

with open(HERE +'/requirements.txt') as f:

    required = f.read().splitlines()
    setup(
        name='pyinstant',
        version='0.0.1',
        description="A real time data streaming and caching library built on top of Redis",
        url="https://github.com/MaddoxMaila/py-instant",
        author="Tshepang Maddox Maila",
        author_email="maila.tshepang719@gmail.com",
        license="MIT",
        zip_safe=False,
        packages=find_packages(),
        include_package_data=True,
        install_requires=required
    )