from django.contrib import admin
from .models import BlogPost
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = (
            "blog_title",
            "author",
            "blog_content",
    )


admin.site.register(BlogPost)

