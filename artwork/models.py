from django.contrib.auth.models import User
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    icon = models.ImageField(upload_to='files/category_icon/')
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Artwork(models.Model):
    author = models.OneToOneField(User)
    type = models.ForeignKey(Type)
    category = models.ForeignKey(Category)
    miniature = models.ImageField(upload_to='files/artworks/')
    description = models.TextField()
    attachment = models.FileField(upload_to='files/attachments/')
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title
