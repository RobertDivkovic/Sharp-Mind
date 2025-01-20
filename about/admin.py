from django.contrib import admin
from .models import About, CollaborationRequest

# Register the About model
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

# Register the CollaborationRequest model
@admin.register(CollaborationRequest)
class CollaborationRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on', 'user')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_on',)