from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['content', 'encrypted', 'encryption_key']

    encryption_key = forms.CharField(required=False, widget=forms.PasswordInput())
