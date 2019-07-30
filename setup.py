import sys
import os
import io
from pathlib import Path
from setuptools import setup, find_packages

# allow setup.py to be run from any path
here = Path(__file__).resolve().parent
os.chdir(str(here))

with io.open("README.md", encoding="utf-8") as readme:
    README = readme.read()

setup(name="CENTAUR",
      description="Hybrid power system simulation program",
      long_description=README,
      platforms="any",
      version="1.0.1",
      license="BSD",
      packages=find_packages(where="."),
      install_requires=["scipy",
                        "matplotlib",
                       ],
      zip_safe=False,
     )
