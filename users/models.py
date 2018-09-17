from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.


class Users(AbstractUser):
    nickname = models.CharField("昵称",max_length=50,blank=True,null=True)
    mobile = models.CharField("手机号码",max_length=11,blank=True,null=True)
    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:userprofile',kwargs={'pk':self.pk})