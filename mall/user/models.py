from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username=models.CharField('用户名',max_length=20,primary_key=True)
    nickname=models.CharField('昵称',max_length=20)
    email=models.EmailField('邮箱')
    password=models.CharField(max_length=32)
    info=models.CharField('个人简介',max_length=150,default='')
    avatar=models.ImageField(upload_to='avatar',null=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    phone=models.CharField(max_length=11,default='')