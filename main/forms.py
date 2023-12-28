from django import forms
from  . models import Document
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','password']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)