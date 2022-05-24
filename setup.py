import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simstring-fast",
    version="0.0.1",
    author="Ruben Menke",
    author_email="ruben.m.menke@gmail.com",
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
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    extras_require = {
        "mongo" : ["pymongo",],
        "mecab" : ["MeCab"],
    }

)
