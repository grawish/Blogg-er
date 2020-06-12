from django.shortcuts import render, HttpResponse, redirect
from blog.models import Blogpost, Blogcomment
from django.contrib import messages
from blog.templatetags import extras


# Create your views here.

def search(query):
    allpost = Blogpost.objects.all()
    returned = []
    for post in allpost:
        if post.Content.lower().__contains__(query) or post.title.lower().__contains__(
                query) or post.author.lower().__contains__(query) or post.slug.lower().__contains__(query):
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
    replydict = {}
    allposts = Blogpost.objects.all()
    mypost = ""
    comment = ""
    exist = False
    if Blogpost.objects.filter(slug=slug).exists():
        mypost = Blogpost.objects.filter(slug=slug).first()
        print(mypost)
        comment = Blogcomment.objects.filter(post=mypost, parent=None)
        replies = Blogcomment.objects.filter(post=mypost).exclude(parent=None)
        for reply in replies:
            if reply.parent.sno not in replydict.keys():
                replydict[reply.parent.sno] = [reply]
            else:
                replydict[reply.parent.sno].append(reply)
    return render(request, 'blog/blogPost.html', {'post': mypost, 'comments': comment, 'replydict': replydict})


def postcomment(request):
    if request.method == "POST":
        text = request.POST.get('comment')
        user = request.user
        postno = request.POST.get('sno')
        post = Blogpost.objects.filter(sno=postno).first()
        parent = request.POST.get('parent')
        if parent == '':
            comment = Blogcomment(text=text, user=user, post=post)
            messages.success(request,
                             "Your valuable thoughts are saved in our data servers and are visible for others!")
        else:
            parent = Blogcomment.objects.filter(sno=parent)[0]
            comment = Blogcomment(text=text, user=user, post=post, parent=parent)
            messages.success(request,
                             "Your valuable thoughts on someone else's thought are saved in our data servers and are "
                             "visible for others!")
        comment.save()

    return redirect(f"/blog/{post.slug}")
