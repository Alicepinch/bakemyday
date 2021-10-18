from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import BlogPost
from .forms import BlogForm

# Create your views here.

def blog(request):
    """ A view to show blog posts details """

    blogposts = BlogPost.objects.all()

    context = {
        'blogposts': blogposts,
    }

    return render(request, 'blog/blog.html', context)


def add_blogpost(request):

    """ Adds a blogpost to the blog section """
    form = BlogForm()
    template = 'blog/add-blogpost.html'
    context = {
        'form': form,
    }

    return render(request, template, context)