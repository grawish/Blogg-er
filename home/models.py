from django.db import models


# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=10, default="")
    desc = models.TextField(max_length=500, default="")
    Timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from '+self.name+' '+self.email+' on '+str(self.Timestamp)