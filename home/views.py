from django.shortcuts import render, HttpResponse
from home import models

# Create your views here.

def home(index):
    return render(index, 'home/home.html')


def about(index):
    return render(index, 'home/about.html')


def contact(index):
    if index.method == 'POST':
        name = index.POST.get('contname')
        email = index.POST.get('contmail')
        phone = index.POST.get('contno')
        desc = index.POST.get('contdesc')
        xcontact = models.Contact(name=name, email=email, contact=phone, desc=desc)
        xcontact.save()
    return render(index, 'home/contact.html')
