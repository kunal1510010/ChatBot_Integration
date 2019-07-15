from django import forms

class InputForm(forms.Form):
    question = forms.CharField(required=True, label="Question", max_length=200,
                               widget=forms.TextInput(attrs={'placeholder': 'Ask Me Something'}))

class AnswerForm(forms.Form):
	answer = forms.CharField(required=True, label="Answer", max_length=200,
                               widget=forms.TextInput(attrs={'placeholder': 'Kindly add the reply to your Question'}))
