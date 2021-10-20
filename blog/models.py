from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(
        max_length=60, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    blog_preview = models.CharField(
        max_length=260, null=True, blank=True)
    blog_body = models.TextField()
    image_url = models.URLField(
        max_length=2048, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True)


    def __str__(self):
        return self.blog_title

