from django import forms
from secapp.models import student

class studform(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
