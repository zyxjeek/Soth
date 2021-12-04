from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/<int:blog_id>', views.blog, name='blog'),
    path('new_blog', views.new_blog, name='new_blog'),
    path('blogs/<int:blog_id>/edit', views.edit_blog, name='edit_blog'),
    path('about', views.about, name="about")
]
