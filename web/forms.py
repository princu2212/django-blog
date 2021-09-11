from django.forms import ModelForm, Form
from django import forms

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ContactForm(Form):
    subject = forms.CharField(max_length=50)
    from_email = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200, widget=forms.Textarea)

class UploadForm(Form):
    file = forms.FileField()