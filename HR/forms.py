from django import forms
from Myapp.models import Category,Job
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['categoryname']

class Jobform(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        