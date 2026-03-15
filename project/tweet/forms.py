from django import forms
from . models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User         

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        

# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     email = forms.EmailField()
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         password1 = cleaned_data.get("password1")
#         password2 = cleaned_data.get("password2")

#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords do not match.")
