from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import BlogPost
from .forms import NewBlogForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required()
def blogs(request):
    b = BlogPost.objects.filter(public=True)
    return render(request, 'blogs.html', context={'blogs': b})


@login_required()
def blog(request, blog_id):
    b = BlogPost.objects.get(id=blog_id)
    return render(request, 'blog.html', context={'blog': b})


@login_required()
def new_blog(request):
    user = request.user
    if request.method == 'POST':
        form = NewBlogForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = user
            topic.save()
            return redirect('blogs')
    else:
        form = NewBlogForm()
    return render(request, 'new_blog.html', locals())


@login_required()
def edit_blog(request, blog_id):
    b = BlogPost.objects.get(id=blog_id)
    if b.user != request.user:
        return Http404
    if request.method != 'POST':
        form = NewBlogForm(instance=b)
    else:
        form = NewBlogForm(instance=b, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')

    return render(request, 'edit_blog.html', locals())


@login_required()
def about(request):
    return render(request, 'about.html')
