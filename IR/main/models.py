from django.db import models

# Create your models here.
class FanFiction(models.Model):
    movie = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    passage = models.TextField()

    def __str__(self):
        return "{} by {}".format(self.title, self.author)