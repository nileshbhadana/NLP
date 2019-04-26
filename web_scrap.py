#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 02:00:08 2019

@author: nilesh
"""

import requests,html5lib
import matplotlib.pyplot as plt
#from nltk import sent_tokenize
from nltk import word_tokenize
from bs4 import BeautifulSoup
#from nltk.stem import PorterStemmer

def remove_dupli(ori_list):
    new_list=[]
    for i in ori_list:
        if i not in new_list:
            new_list.append(i)
    
    return new_list

        


url="https://en.wikipedia.org/wiki/Superman"
#url="https://en.wikipedia.org/wiki/Nilesh"
r=requests.get(url)
#print(r.content)

soup=BeautifulSoup(r.content,'html5lib')
#print(soup.prettify())

quotes=[]  # a list to store quotes 
  
#table = soup.find('div', attrs = {'id':'container'}) 
#table=soup.find_all('div',class_="mw-parser-output")
tables=soup.find_all('div',class_="mw-body-content")
#print(tables[2])
data=tables[2].getText()
#data="men men men in in"
#sent_token=sent_tokenize(data)
word_token=word_tokenize(data)
#print(word_token)

new_list=remove_dupli(word_token)
#new_list=['super','is','man','hero','was']

freq=[]
for i in new_list:
    counter=word_token.count(i)
    freq.append(counter)
    
print(new_list)
print(freq)

#print("plotting graph")
#plt.bar(new_list,freq)
#plt.show()

'''
stem=PorterStemmer()

for i in range(len(sent_token)):
    words=word_tokenize(sent_token[i])
    new_word=[stem.stem(word) for word in words]
        #print(stem.stem(word))
    print(new_word)
    #new_data=" ".join(new_word)
    #print(new_data)



names=[]
for name in table:
    names.append(name.get('title'))

for row in soup.find_all('ul'): 
    quote = {} 
    #print(row.get('href'))
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.h6.text 
    quote['author'] = row.p.text 
    quotes.append(quote) 
    
print(quotes)

for nam in names:
    print(nam)
'''
