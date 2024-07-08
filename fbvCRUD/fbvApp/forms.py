from django import forms
from fbvApp.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'