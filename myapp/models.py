from django.db import models


class Post(models.Model):
    title= models.CharField(max_length=300, blank=True)
    content= models.TextField()