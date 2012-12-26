#coding:utf-8
import random

data_size = 100000
min_strings_length = 6
max_strings_length = 6
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in xrange(0,data_size) :
    strings_length = random.randint(min_strings_length, max_strings_length)
    strings = ""
    for j in xrange(0, strings_length) :
        id_alphabet = random.randint(0,len(alphabet)-1)
        strings += alphabet[id_alphabet]
    print strings
