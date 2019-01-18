#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:24:16 2019

@author: nilesh
"""

from nltk.stem import PorterStemmer
from nltk import sent_tokenize
from nltk import word_tokenize

data="hi how are you?"

sent_token=sent_tokenize(data)
stem=PorterStemmer()

for i in range(len(sent_token)):
    words=word_tokenize(sent_token[i])
    new_word=[stem.stem(word) for word in words]
        #print(stem.stem(word))
    print(new_word)
    new_data=" ".join(new_word)
    print(new_data)