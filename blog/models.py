from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Blogpost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    Content = models.TextField(max_length=10000, default="")
    author = models.CharField(max_length=10, default="")
    slug = models.CharField(max_length=100, default="")
    Timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.sno) + '. ' + self.title + ' by ' + self.author


class Blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    text = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.text[0:13] + '..... by ' + str(self.user.first_name) + ' on ' + self.post.slug
