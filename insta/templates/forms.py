from django import forms
from .models import Profile,Image,Comment
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['owner']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =['likes','profile']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'comment_owner']