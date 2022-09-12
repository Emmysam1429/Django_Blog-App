from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title