from django.db import models
import uuid


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='Authors ID')
    email = models.EmailField(verbose_name='Email Address', unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='Avatars/', width_field=300, height_field=300)
    date_joined = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    content = models.CharField(max_length=350)
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Articles/')

