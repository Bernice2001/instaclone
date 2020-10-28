from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.TextField(default="Anonymous")
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    def save_profile(self):
        self.user
    def delete_profile(self):
        self.delete()
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(owner=id)
        return profile
    # @classmethod
    # def search_profile(cls, name):
        # return cls.objects.filter(user__username__icontains=name).all() class Profile(models.Model):

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True, null=True)
    profile= models.ForeignKey(User, blank=True,on_delete=models.CASCADE)


    class Meta:
        ordering = ["-pk"]

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

class Comment(models.Model):
    #image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='comment')
   # comment_owner = models.ForeignKey(User, blank=True)
    #comment= models.TextField()
    def save_comment(self):
        self.save()
    def delete_comment(self):
        self.delete()
    @classmethod
    def get_image_comments(cls, id):
        comments = Comment.objects.filter(image__pk=id)
        return comments
    def __str__(self):
        return str(self.comment)        