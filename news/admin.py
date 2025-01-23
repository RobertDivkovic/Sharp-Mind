from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Post, Comment, Category, ContactSubmission, Profile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Number of empty comment forms to display


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "author")
    list_filter = ("status", "created_on", "categories")
    search_fields = ["title", "content", "excerpt"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)  # Apply Summernote to the 'content' field
    ordering = ('-created_on',)
    inlines = [CommentInline]
    list_editable = ("status",)  # Allow inline editing of the status field


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("get_user_or_author", "email", "body", "post",
                    "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("author", "user__username", "email", "body")
    actions = ["approve_comments"]
    ordering = ('-created_on',)  # Comments will also be ordered by most recent
    list_editable = ("approved",)  # Allow inline editing of the approved field

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    def get_user_or_author(self, obj):
        """
        Display the associated user if available;
        otherwise, fall back to the author field.
        """
        return obj.user.username if obj.user else obj.author
    get_user_or_author.short_description = "User/Author"


# Register Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_on')
    search_fields = ('name', 'email', 'subject', 'message')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    search_fields = ('user__username',)  # Allow searching by username
    list_filter = ('user__is_active',)  # Add filters based on user status
    fields = ('user', 'profile_picture')
    ordering = ('user__username',)


# Inline for Profile (to edit profile picture in user details)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False  # Prevent accidental deletion of profiles
    verbose_name_plural = 'Profile'
    fields = ('profile_picture',)  # Allow editing the profile picture


# Custom UserAdmin to include ProfileInline
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)  # Add the ProfileInline to UserAdmin

    # Optional: Add additional display fields or filters
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')


# Unregister the default UserAdmin and register the customized version
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Added these lines here for custom admin titles
admin.site.site_header = "Sharp-Mind Admin"
admin.site.site_title = "Sharp-Mind Admin Panel"
admin.site.index_title = "Welcome to the Sharp-Mind Admin Panel"
