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
    message_name = forms.CharField(max_length=50)
    message_email = forms.EmailField(max_length=150)
    message_content = forms.CharField(widget=forms.Textarea, max_length=2000)
