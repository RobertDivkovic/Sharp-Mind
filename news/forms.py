from django import forms
from .models import Comment, ContactSubmission, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'featured_image', 'content', 'categories', 'status']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
            'categories': forms.CheckboxSelectMultiple(),
        }