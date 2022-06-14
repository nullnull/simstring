from .character_ngram import CharacterNgramFeatureExtractor
from .word_ngram import WordNgramFeatureExtractor

# MeCab cannot be provided witha  cleaner API due to the lacking typing support of MeCab
# try:
#     from .mecab_ngram import MecabNgramFeatureExtractor
# except ModuleNotFoundError:
#     pass
