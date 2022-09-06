from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ContactForm(forms.Form):
    message_name = forms.CharField(max_length=50)
    message_email = forms.EmailField(max_length=150)
    message_content = forms.CharField(widget=forms.Textarea, max_length=2000)