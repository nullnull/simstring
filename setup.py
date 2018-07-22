import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simstring",
    version="0.0.1",
    author="Katsuma Narisawa",
    author_email="katsuma.narisawa@gmail.com",
    description="A Python implementation of the SimString, a simple and efficient algorithm for approximate string matching.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
