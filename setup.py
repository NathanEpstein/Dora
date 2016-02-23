from setuptools import setup

setup(
  name = "Dora",
  version = "0.0.1",
  author = "Nathan Epstein",
  author_email = "ne2210@columbia.edu",
  description = ("Exploratory data analysis toolkit for Python"),
  license = "MIT",
  keywords = "exploratory data analysis",
  install_requires = [
    "matplotlib>=1.5.1",
    "sklearn",
    "scipy>=0.17.0",
    "numpy",
    "pandas>=0.17.1",
  ]
)