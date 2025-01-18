from django.contrib import admin
from .models import Post, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "author")
    list_filter = ("status", "created_on")
    search_fields = ["title", "content", "excerpt"]
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "email", "body", "post", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("author","email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)