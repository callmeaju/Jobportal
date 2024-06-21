from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Myapp.models  import Student

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email']

# class LoginForm(forms.Form):
#     Username = forms.CharField()
#     Password = forms.CharField()

class Studentprofile(forms.ModelForm):
    class Meta:
        model = Student
        exclude =("user",)
        fields = '__all__'


