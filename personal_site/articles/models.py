from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title