from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Number of empty comment forms to display

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "author")
    list_filter = ("status", "created_on")
    search_fields = ["title", "content", "excerpt"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)  # Apply Summernote to the 'content' field
    ordering = ('-created_on',)  # This sets the default order in the admin panel
    inlines = [CommentInline]
    list_editable = ("status",)  # Allow inline editing of the status field

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("get_user_or_author", "email", "body", "post", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("author", "user__username", "email", "body")
    actions = ["approve_comments"]
    ordering = ('-created_on',)  # Comments will also be ordered by most recent
    list_editable = ("approved",)  # Allow inline editing of the approved field

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    def get_user_or_author(self, obj):
        """
        Display the associated user if available; otherwise, fall back to the author field.
        """
        return obj.user.username if obj.user else obj.author
    get_user_or_author.short_description = "User/Author"

# Added these lines here for custom admin titles
admin.site.site_header = "Sharp-Mind Admin"
admin.site.site_title = "Sharp-Mind Admin Panel"
admin.site.index_title = "Welcome to the Sharp-Mind Admin Panel"