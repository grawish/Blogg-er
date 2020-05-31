from django.shortcuts import render, HttpResponse
from home import models
from django.contrib import messages


# Create your views here.

def home(index):
    return render(index, 'home/home.html')


def about(index):
    return render(index, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('contname')
        email = request.POST.get('contmail')
        phone = request.POST.get('contno')
        desc = request.POST.get('contdesc')
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(desc) < 4:
            messages.error(request, 'Please fill the form correctly!')
        else:
            messages.success(request, 'Form has been filled successfully!')
            xcontact = models.Contact(name=name, email=email, contact=phone, desc=desc)
            xcontact.save()

    return render(request, 'home/contact.html')
