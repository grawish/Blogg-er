from django.shortcuts import render, HttpResponse


# Create your views here.


def BlogHome(request):
    return render(request, 'blog/blogHome.html')


def BlogPost(request, slug):
    return render(request, 'blog/blogPost.html')
