#!pip install jsonmerge
from jsonmerge import merge
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
    print(result)
    return' '.join((result))

def chatbot_function(user_input):
	user_input = user_input.lower()
	uinput = naturalprocessing(user_input)
	try:
		return random.choice(final_data[uinput])
	except KeyError:
		return "Sorry, I didn't get you"

def chat(uinput):
	if uinput=='quit' or uinput=='bye' or uinput=='exit':
		return ("Thanks for the communication. Looking forward to meet you again.")
		
	else:
		result = chatbot_function(uinput)
		return result


