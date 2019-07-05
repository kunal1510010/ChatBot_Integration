import json
import os
import random
from ast import literal_eval

import spacy
nlp = spacy.load('en_core_web_sm')

def text_extractor(string):
    string = string.replace('\\','')
    string = string.replace('\n','')
    string = literal_eval(string)
    return string['conversations']

def tokenizer(temp):
    result = []
    for i in temp:
        if i.is_stop!=True:
            result.append(i.lemma_)
    return ' '.join(result)

def stopwords_removal(file):
    temps = text_extractor(open(file,'r').read())
    keys = temps.keys()
    data = {}
    for i in keys:
        temp = nlp(i)
        a = tokenizer(temp)
        a = a.lower()
        if a not in data:
            data[a] = temps[i]
    return data

final = {}
for files in os.listdir():
    if files.endswith('.json'):
        if files[:6] != 'corpus':
            a = stopwords_removal(files)
            temp = json.loads(open(files).read())
            final = {'categories' : temp['categories'],
                    'sub categories' : temp['sub categories'],
                     'conversations' : a}
            with open('corpus_'+files , 'w') as f:
                json.dump(final,f)
