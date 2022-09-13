"""
Imports for forms functionality
"""

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Comment form
    """
    class Meta:
        """
        Take Comment model and diplay 'body' field
        """
        model = Comment
        fields = ('body',)


class ContactForm(forms.Form):
    """
    Contact form
    """
    message_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    message_email = forms.CharField(
        max_length=100, widget=forms.EmailInput(
            attrs={'placeholder': 'Email Address'}))
    message_content = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Message'}), max_length=2000)
