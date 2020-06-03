from django.db import models


# Create your models here.

class Blogpost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    Content = models.TextField(max_length=10000, default="")
    author = models.CharField(max_length=10, default="")
    slug = models.CharField(max_length=100, default="")
    Timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.sno) + '. ' + self.title + ' by ' + self.author


class comment(models.Model):
    sno = models.AutoField(primary_key=True)
    text = models.TextField(max_length=1000)
    user = models.CharField(max_length=20)
    blog = models.CharField()
    parent = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
