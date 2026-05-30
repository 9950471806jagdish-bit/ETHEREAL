from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Profile(models.Model):
    userprofile = models.OneToOneField(User, on_delete=models.CASCADE)
    # We added null=True and blank=True so you don't have to provide a default during migrations
    Username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)  # Increased length for bio
    gender = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default='profile.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.userprofile.username} Profile'

    def save(self, *args, **kwargs):
        try:
            this = Profile.objects.get(id=self.id)
            if this.image != self.image and this.image.name != 'profile.jpg':
                if os.path.isfile(this.image.path):
                    os.remove(this.image.path)
        except Profile.DoesNotExist:
            pass
        super(Profile, self).save(*args, **kwargs)

class Post(models.Model):
    post_image = models.ImageField(default='post.jpg', upload_to='post_pics')

    def __str__(self):
        return f'Post {self.id}'

    def save(self, *args, **kwargs):
        try:
            this = Post.objects.get(id=self.id)
            if this.post_image != self.post_image and this.post_image.name != 'post.jpg':
                if os.path.isfile(this.post_image.path):
                    os.remove(this.post_image.path)
        except Post.DoesNotExist:
            pass
        super(Post, self).save(*args, **kwargs)