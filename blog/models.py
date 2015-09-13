from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=20)


class Images(models.Model):
    image = models.ImageField(upload_to='img')
