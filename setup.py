  
from setuptools import find_packages, setup

setup(name='pyutils',
      version='0.1.1',
      description='Helper functions for pandas and other python tasks',
      url='https://github.com/clryan/pyutils',
      author='Claire Ryan',
      author_email='ryan.claire29@gmail.com',
      license='MIT',
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      zip_safe=False)
