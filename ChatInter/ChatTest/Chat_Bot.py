from nltk.chat.util import Chat, reflections
from random import randint

global token,universal_list
token = 0
universal_list = []

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}

pairs=[
[r"my name is (.*)|hi i am (.*)",["Hello %1, How are you today ?","Hello %2, How are you today ?"]],
[r"i am good|i am fine|i am okay|i am ok",["Nice to hear that",]],
[r"what is your name ?",["My name is EduBot and I'm a chatbot",]],
[r"how are you ?",["I'm doing good\nHow about You ?",]],
[r"sorry (.*)",["Its alright","Its OK, never mind",]],
[r"i'm (.*) doing good",["Nice to hear that","Alright :)",]],
[r"hi|hey|hello",["Hello", "Hey there",]],
[r"(.*) age?|(.*)old are you?",["I'm a computer program dude\nSeriously you are asking me this?",]],
[r"what (.*) want ?",["Make me an offer I can't refuse",]],
[r"(.*) created ?",["Edugrad created me","Top secret ;)",]],
[r"(.*) (location|city|located) ?",['Hyderabad, Noida',]],
[r"(.*) (weather)",["Weather is awesome like always","Too hot man here in"]],
[r"i work in (.*)?",["%1 is an Amazing company, I have heard about it.",]],
[r"(.*)raining in (.*)",["No rain since last week here in %2","Damn its raining too much here in %2"]],
[r"how (.*) health(.*)",["I'm a computer program, so I'm always healthy ",]],
["(.*) (sports|game) ?",["I'm a very big fan of Football",]],
[r"who|which (.*) player|sportsman ?",["Messy","Ronaldo","Roony"]],
[r"who (.*) (moviestar|actor)?",["Shah Rukh Khan"]],
# [r"who (.*) (moviestar|actor)?",["Brad Pitt"]],
# [r"who (.*) (moviestar|actor)?",["Brad Pitt"]],
# [r"who (.*) (moviestar|actor)?",["Brad Pitt"]],
# [r"who (.*) (moviestar|actor)?",["Brad Pitt"]],
[r"(.*) scope of data science | (.*) scope of Data Scientist|(.*) scope of data analyst|(.*) scope of data analysis",["Data Scientist or Data Analyst is the most trending field nowadays. Several companies are hiring "]],
[r"what is ai?",["In computer science, artificial intelligence, sometimes called machine intelligence, is intelligence demonstrated by machines",]],
[r"quit|exit",["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]],
[r"(.*) (data science)",["Data science is a multi-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data."]],
]


def random():
    range_start = 10**(7-1)
    range_end = (10**7)-1
    return randint(range_start, range_end)

def chatty(user_input):
    chat = Chat(pairs, reflections)
    file = open("none_values.txt","a+")
    if chat.respond(user_input) == None:
    	# print("EduBot: ",chat.respond(user_input))
    	file.write(user_input + "\n")
    	return None
    else:
    	# print("EduBot: ",chat.respond(user_input))
    	return chat.respond(user_input)

def non_technical():
	print("Choose from below options your problem\n")
	print("1. Assignment is locked or Unable to Submit the Assignment")
	print("2. Quiz is still locked")
	print("3. Providing Certificate after course completion")
	print("4. Didn't recieve mail after submitting assignment")
	print("5. Extension of Assignment Date")
	print("6. I want to resubmit assignment")
	problem = input("Enter you problem: ")
	num = random()
	if num not in universal_list:
		universal_list.append(num)
		print(problem)
		return ("You issue has been successfully saved. Your token generated is: " + str(num) + "Sit back and take a drink. Our SME will soon get back to you with relevant solution")


def technical():
	print("Please elaborate the difficulty you are facing\n Take a drink and set back. Meanwhile we'll get back to you.")
	user  = input("Enter your issue: ")
	num = random()
	if num not in universal_list:
		universal_list.append(num)
		print(user)
		return "You issue has been successfully saved. Your token generated is: " + str(num)


def chatbot_function(user_input):
	# import time
	# from tqdm import tqdm
	# for i in tqdm(range(10)):
	# 	time.sleep(0.09)
	print("Hi, I'm EduBot and I chat alot") #default message at the start
	print("To start a conversation with me start typing and for other queries choose appropriate tab")
	print("---------------------------------------------")
	print("1. Assignments/ Quiz Submission and Deadline Extension related Queries")
	print("2. Technical Queries such as Coding Problem")
	print("3. Assignment Questions Guidance Related Queries")
	print("4. Others")
	print("Enter your choice from 1 to 4 and to communicate with bot start typing")
	while True:
		user_input = user_input.strip()
		if user_input == 'quit' or user_input == 'exit': 
			break
		elif user_input == '1':
			k = non_technical()
		elif user_input == '2':
			k = technical()
		elif user_input == '3':
			k = assignment()
		elif user_input == '4':
			k = others()
		else:
			k = chatty(user_input)
		return k

#user_input = input("USER: ")
#result = chatbot_function(user_input)
#print("Edubot: ",result)


