from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


def blog_detail(request, blogpost_id):
    """ A view to display blog detail page"""

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    context = {
        'blogpost': blogpost,
    }

    return render(request, 'blog/blog-detail.html', context)


def add_blogpost(request):
    """ Adds a blogpost to the blog section """

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, you can only add a blog post if you are a registered user!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New blogpost added')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add blogpost 😔 Please check the form is valid.')
    else:
        form = BlogForm()
    
    form = BlogForm()
    template = 'blog/add-blogpost.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def delete_blogpost(request, blogpost_id):
    """ Deletes blog post from blog section"""

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)

    if request.user.is_superuser or request.user == blogpost.author:
        blogpost.delete()
        return redirect(reverse('blog'))
    else:
        messages.error(request, "Sorry, you didn't create this blogpost so you can't delete this")
        return redirect(reverse('blog'))