# Generated by Django 2.2.12 on 2021-01-15 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户名')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('password', models.CharField(max_length=32)),
                ('info', models.CharField(default='', max_length=150, verbose_name='个人简介')),
                ('avatar', models.ImageField(null=True, upload_to='avatar')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(default='', max_length=11)),
            ],
        ),
    ]