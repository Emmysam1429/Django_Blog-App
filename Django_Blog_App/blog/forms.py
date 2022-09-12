from dataclasses import fields
# from pyexpat import model
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('author_name','title','content','create_date','publish_date')



class userRegistationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')



