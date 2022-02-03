from django.contrib import admin
from BLOG.models import Post, BlogComment
# Register your models here.

admin.site.register((Post, BlogComment))