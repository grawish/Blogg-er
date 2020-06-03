from django.shortcuts import render, HttpResponse
from blog.models import Blogpost
from django.contrib import messages


# Create your views here.

def search(query):
    allpost = Blogpost.objects.all()
    returned = []
    for post in allpost:
        if post.Content.lower().__contains__(query) or post.title.lower().__contains__(
                query) or post.author.lower().__contains__(
            query) or post.slug.lower().__contains__(query):
            returned.append(post)
    return returned


def BlogHome(request):
    allposts = Blogpost.objects.all()
    if request.method == 'POST':
        query = request.POST.get('search')
        if len(query) >= 40:
            allposts = []
        else:
            allpoststitle = Blogpost.objects.filter(title__icontains=query)
            allpostsslug = Blogpost.objects.filter(slug__icontains=query)
            allpostscontent = Blogpost.objects.filter(Content__icontains=query)
            allpostsauthor = Blogpost.objects.filter(author__icontains=query)
            allposts = allpoststitle.union(allpostsauthor, allpostscontent, allpostsslug)

        if len(allposts) == 0:
            print('zero')
            messages.warning(request, "Please search Correctly!")
    return render(request, 'blog/blogHome.html', {'allposts': allposts})


def BlogPost(request, slug):
    allposts = Blogpost.objects.all()
    mypost = ""
    exist = False
    if Blogpost.objects.filter(slug=slug).exists():
        mypost = Blogpost.objects.filter(slug=slug).first()
        exist = True
        print(mypost)
    return render(request, 'blog/blogPost.html', {'post': mypost, 'exist': exist})
