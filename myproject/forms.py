from django import forms
from .models import Book
from.models import Contact
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 



class RegisterForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput)
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password1','password2']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'



