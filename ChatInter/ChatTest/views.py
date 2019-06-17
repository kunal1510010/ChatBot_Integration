from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import InputForm
import Chat_Bot


def main(request):
    form = InputForm()

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_query = form.cleaned_data['question']
            bot_response = Chat_Bot.chatbot_function(str(user_query))
            return render(request, 'main.html', {'form': form, 'message': bot_response})
        else:
            return HttpResponseRedirect('/test/')

    initial_message = 'Hey there, I am Edubot. I\'m in Beta phase right now so will not be able to answer much but ' \
                      'once complete I\'ll be of great help, so please stick to relevant questions and help me improve ' \
                      'myself '
    return render(request, 'main.html', {'form': form, "message": initial_message})
