
from django.contrib import admin
from .models import BlogPost, Tag

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'minutes_to_read')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    search_fields = ('title', 'content')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)