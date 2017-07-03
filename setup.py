from description import __version__, __author__
from setuptools import setup, find_packages

setup(
   name="fastcosine",
   version=__version__,
   author=__author__,
   author_email='soy.lovit@gmail.com',
   url='https://github.com/lovit/fastcosine',
   description="Approximated nearest neighbor search indexer for sparse vector",
   long_description="""Approximated nearest neighbor search indexer for sparse vector""",
   keywords = ['approxinated nearest neighbor search inverted indexer'],
   packages=find_packages()
)
