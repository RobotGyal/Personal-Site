from django.db import models
from django.conf import settings


# Create your models here.
class Code(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    img = models.ImageField(upload_to='pics/') 
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    repo_url = models.URLField(max_length=200)
    live_url = models.URLField(max_length=200)
    technologies = models.TextField()


    def __str__(self):
        return self.title