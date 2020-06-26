from django.db import models
from django.conf import settings


# Create your models here.
class Website(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics/') 
    live_url = models.URLField(max_length=200)
    repo_url = models.URLField(max_length=200)
    summary = models.TextField()
    created_on = models.DateTimeField(auto_now_add=False)
    built_with = models.TextField()

    def __str__(self):
        return self.title