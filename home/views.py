from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from home import models
from blog.models import Blogpost
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def home(index):
    allposts = Blogpost.objects.all()

    return render(index, 'home/home.html', {'allposts': allposts})


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


def handlesignup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pas = request.POST.get('pas')
        pasc = request.POST.get('pasc')
        # check for inputs
        if len(uname) > 20:
            messages.error(request, "username must not be above 10 characters")
        if pas != pasc:
            messages.success(request, "Passwords Do not Match!")
        # create user
        myuser = User.objects.create_user(uname, email, pas)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "You are now a member of icoder family")
        return redirect('home')
    else:
        return HttpResponse("You are not supposed to be here!")


def handlelogin(request):
    if request.method == "POST":
        user = request.POST.get("uname")
        passwd = request.POST.get("lpas")
        myuser = authenticate(username=user, password=passwd)
        if myuser is not None:
            print("authenticate!")
            login(request, myuser)
            messages.success(request, "You successfully entered the world of icoder!")
            return redirect('home')
        else:
            print("no authenticate!")
            messages.error(request, "You are not authorised to enter the world of icoder")
            return redirect('home')
    return HttpResponse("login")


def handlelogout(request):
    logout(request)
    messages.success(request, "Logout successful! Please come back to explore more!")
    return redirect('home')
