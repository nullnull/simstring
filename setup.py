import setuptools

# for development mode
try:
    from mypyc.build import mypycify
except:
    def mypycify(A):
        return None


with open("README.md", "r") as fh:
    long_description = fh.read()

# from simstring.searcher import version
version = "0.1.0"

setuptools.setup(
    name="simstring-fast",
    author="Banking Circle",
    description="A fork of the Python implementation of the SimString by (Katsuma Narisawa), a simple and efficient algorithm for approximate string matching. Uses mypyc to improve speed",
    version=version,
    author_email="advancedanalytics@bankingcircle.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/icfly2/simstring-fast",
    project_urls={
        'Documentation': 'https://icfly2.github.io/simstring-fast/',
        'Funding': 'https://www.bankingcircle.com/',
        'Source': 'https://github.com/icfly2/simstring-fast',
        'Tracker': 'https://github.com/icfly2/simstring-fast/issues',
    },
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require = {
        "mongo" : ["pymongo",],
        "mecab" : ["MeCab"],
    },
    ext_modules=mypycify([
        'simstring/__init__.py',
        'simstring/searcher.py',

        'simstring/feature_extractor/base.py',
        'simstring/feature_extractor/character_ngram.py',
        'simstring/feature_extractor/word_ngram.py',

        'simstring/database/base.py',
        'simstring/database/dict.py',
        # 'simstring/database/mongo.py',

        'simstring/measure/base.py',
        'simstring/measure/overlap.py',
        'simstring/measure/cosine.py',
        'simstring/measure/dice.py',
        'simstring/measure/jaccard.py',
        
    ]),

)
