from django import forms

class InputForm(forms.Form):
    question = forms.CharField(required=True, label="Question", max_length=200,
                               widget=forms.TextInput(attrs={'placeholder': 'Ask Me Something'}))

