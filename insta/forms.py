from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.files.images import get_image_dimensions
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'like']
         
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','post']
