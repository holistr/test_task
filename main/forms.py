from django import forms
from main.models import Contact


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    class Meta:
        model = Contact
        fields = '__all__'
