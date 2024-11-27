from django import forms
from .models import*

class normal_form(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()
    place=forms.CharField()

class model_form(forms.ModelForm):
    
    class Meta:
     model=project_user
     fields = '__all__'
