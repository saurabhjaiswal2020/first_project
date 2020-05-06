from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=255, unique=False)
    email = models.EmailField(unique=False,max_length=50)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name





class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username