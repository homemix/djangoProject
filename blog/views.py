from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'the wolf',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'March 23,2021'
    },
    {
        'author': 'the wolf tech',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'March 23,2021'
    },
]


# Create your views here.
def home(request):
    context ={
        'posts':posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
