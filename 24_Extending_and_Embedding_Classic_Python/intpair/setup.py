from setuptools import setup, Extension
setup(name='intpair',
      ext_modules=[Extension('intpair',sources=['intpair.c'])])
