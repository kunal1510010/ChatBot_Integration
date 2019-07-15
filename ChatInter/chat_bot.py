#!pip install jsonmerge
#!pip install datetime
from jsonmerge import merge
import json

from datetime import date

import os
import random

from ast import literal_eval

import re

import spacy
nlp = spacy.load('en_core_web_sm')

def custom_stop_words():
    words = ['tell','show','me','u','s']
    for i in words:
        nlp.vocab[i].is_stop = True
    nlp.vocab['name'].is_stop = False

def text_extractor(string):
    string = string.replace('\\','')
    string = string.replace('\n','')
    string = literal_eval(string)
    return string['conversations']

a = []
path = 'corpus/'
for files in os.listdir(path):
    if files.endswith('.json'):
        data = text_extractor(open(path + files,'r',encoding="utf8").read())
        a.append(data)
    final_data = {}
for i in a:
    final_data = merge(i,final_data)

def naturalprocessing(user_input):
    ui = nlp(user_input)
    result = []
    for i in ui:
        if i.is_stop!=True:
            result.append(i.lemma_)
    return' '.join(sorted(result))

def chatbot_function(user_input):
    user_input = user_input.lower()
    uinput = naturalprocessing(user_input)
    try:
        if uinput == 'date today':
            return date.today().strftime("Today is %B %d %Y")
        else:
            return random.choice(final_data[uinput])
    except KeyError:
        file = open("none_values.txt","a+")
        file.write(user_input + "\n")
        return 'none'

def chat(uinput):
    uinput = re.sub(r'[^\w\s]',' ',uinput)
    custom_stop_words()
    if uinput=='quit' or uinput=='bye' or uinput=='exit':
        return "Thanks for the communication. Looking forward to meet you again."
    else:
        result = chatbot_function(uinput)
        return result

