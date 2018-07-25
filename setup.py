import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simstring-pure",
    version="1.0.0",
    author="Katsuma Narisawa",
    author_email="katsuma.narisawa@gmail.com",
    description="A Python implementation of the SimString, a simple and efficient algorithm for approximate string matching.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nullnull/simstring",
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
