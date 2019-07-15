from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InputForm, AnswerForm
import chat_bot
import json
import random
input_dict={}

def main(request):
    form = InputForm()
    chat_token = random.randrange(100000, 900000)
    request.session['token'] = chat_token
    initial_message = 'Hey there, I am Edubot. I\'m in Beta phase right now so will not be able to answer much but ' \
                      'once complete I\'ll be of great help, so please stick to relevant questions and help me improve ' \
                      'myself '
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_query = form.cleaned_data['question']
            bot_response = chat_bot.chat(str(user_query))
            if bot_response == 'none':
                request.session['question'] = user_query
                return HttpResponseRedirect('/input')
            input_dict.update({bot_response: user_query})
            request.session['input_msg'] = input_dict
            print(request.session['input_msg'])
            return render(request, 'main.html', {'form': form, 'chat': input_dict, 'message': initial_message})
        else:
            return HttpResponseRedirect('/')
    return render(request, 'main.html', {'form': form, "message": initial_message})


def input_ans(request):
    form = AnswerForm()
    question = request.session['question']

    if request.method == 'POST':

        question = request.session['question']
        form = AnswerForm(request.POST)
        if form.is_valid():
            response = form.cleaned_data['answer']
            file = open("user_response.txt","a+")
            dic = {question:response}
            file.write(str(dic)+ "\n")
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect('/')

    return render(request, 'get_response.html', {'form': form, "question": question})