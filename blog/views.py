from django.shortcuts import render
from .models import BlogPost


# Create your views here.
def index(request):
    return render(request, 'index.html')


def blogs(request):
    b = BlogPost.objects.filter(public=True)
    return render(request, 'blogs.html', context={'blogs': b})


def blog(request, blog_id):
    b = BlogPost.objects.get(id=blog_id)
    return render(request, 'blog.html', context={'blog': b})
