from django import forms
from .models import Email


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('document',)
