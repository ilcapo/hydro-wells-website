from django.contrib import admin
from .models import BlogPost, BlogCategory

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_published', 'category')
    list_filter = ('is_published', 'category', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'published_date'