from django import forms
from .models import BlogPost, BlogComment

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = (
            'blog_title',
            'blog_preview',
            'blog_body',
            'image_url',
            'image',
            )

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = (
            'comment_title',
            'comment'
            )