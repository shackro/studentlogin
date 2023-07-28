from models import watch
from django import forms

class viewform(forms.ModelForm):
    class Meta:
        model = watch
        fields = ['classname ', 'location']