from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    like = models.IntegerField(default=0)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_profile')
    date = models.DateTimeField(auto_now_add=True, null=True)


    class Meta:
        ordering = ["-date"]

    @property
    def get_all_comments(self):
        return self.comments.all()

    def __str__(self):
        return str(self.name)

    def save_image(self):
     self.save()

    def delete_image(self):
     self.delete()

    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk=profile)
        return images 

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    
class Stream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField()
    
    def add_post(sender,instance,*args,**kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)
        
        for follower in followers:
            stream = Stream(post=post, user=follower.follower, date=post.date, following=user)
            stream.save()
            
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')

class Comment(models.Model):
    comment = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
            
