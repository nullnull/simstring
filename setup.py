import setuptools



with open("README.md", "r") as fh:
    long_description = fh.read()

from simstring.searcher import version

setuptools.setup(
    name="simstring-fast",
    version="0.1.0",
    version=version,
    author="Advanced Analytics",
    author_email="advancedanalytics@bankingcircle.com",
    description="A fork of the Python implementation of the SimString by (Katsuma Narisawa), a simple and efficient algorithm for approximate string matching.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/icfly2/simstring-fast",
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    extras_require = {
        "mongo" : ["pymongo",],
        "mecab" : ["MeCab"],
    }

)
