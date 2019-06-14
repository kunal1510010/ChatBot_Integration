from django.shortcuts import render

import Chat_Bot


def main(response):
	
	result= Chat_Bot.chatbot_function('hello')
	print(result)
