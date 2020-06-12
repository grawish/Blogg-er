from django.contrib import admin
from .models import Blogpost, Blogcomment

# Register your models here.
admin.site.register((Blogpost, Blogcomment))
