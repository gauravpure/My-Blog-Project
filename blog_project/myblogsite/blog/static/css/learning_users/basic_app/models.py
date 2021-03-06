from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add any additional attributes you want

    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True)

    def __str__(self):
        # Built-in Attribute of django.contrib.auth.models.UserProfileInfo
        return self.user.username
