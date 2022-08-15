from setuptools import setup, Extension
setup(name='merge',
      ext_modules=[Extension('merge',sources=['merge.c'])])
