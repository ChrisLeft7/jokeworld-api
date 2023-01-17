from django.db import models

# Create your models here.
class Joke(models.Model):
    setup = models.CharField(max_length=200)
    punchline = models.CharField(max_length=200)