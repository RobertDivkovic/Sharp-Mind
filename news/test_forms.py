from django.test import TestCase
from news.forms import CommentForm, ContactForm, PostForm, ProfileForm
from news.models import Comment, ContactSubmission, Post, Profile, Category
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class TestForms(TestCase):

    def test_comment_form_valid(self):
        """Test that the CommentForm is valid with valid data."""
        form = CommentForm(data={'body': 'This is a test comment'})
        self.assertTrue(form.is_valid(), "CommentForm should be valid with a valid body")

    def test_comment_form_invalid(self):
        """Test that the CommentForm is invalid without body data."""
        form = CommentForm(data={'body': ''})
        self.assertFalse(form.is_valid(), "CommentForm should be invalid without a body")

    def test_contact_form_valid(self):
        """Test that the ContactForm is valid with all fields filled."""
        form = ContactForm(data={
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        })
        self.assertTrue(form.is_valid(), "ContactForm should be valid with all fields filled")

    def test_contact_form_invalid(self):
        """Test that the ContactForm is invalid without required fields."""
        form = ContactForm(data={
            'name': '',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': ''
        })
        self.assertFalse(form.is_valid(), "ContactForm should be invalid without required fields")

    from django.core.files.uploadedfile import SimpleUploadedFile

    def test_post_form_valid(self):
        """Test that the PostForm is valid with valid data."""
        user = User.objects.create(username='testuser')
        category = Category.objects.create(name="Test Category", slug="test-category")  # Create a test category

        # Provide a valid featured_image (optional field)
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")

        form = PostForm(data={
            'title': "Test Post",
            'content': "Test content",
            'categories': [category.id],  # Pass category ID(s) as a list
            'status': 1
        }, files={
            'featured_image': image  # Pass the image file if required
        })

        print(form.errors)  # Debugging line
        self.assertTrue(form.is_valid(), "PostForm should be valid with correct data")

    def test_post_form_invalid(self):
        """Test that the PostForm is invalid without a title."""
        form = PostForm(data={
            'title': '',
            'featured_image': None,
            'content': 'Test content',
            'categories': [],
            'status': 1
        })
        self.assertFalse(form.is_valid(), "PostForm should be invalid without a title")

    def test_profile_form_valid(self):
        """Test that the ProfileForm is valid with a profile picture."""
        form = ProfileForm(data={'profile_picture': None})
        self.assertTrue(form.is_valid(), "ProfileForm should be valid with valid data")

    def test_profile_form_invalid(self):
        """Test that the ProfileForm is valid even with no data (if optional)."""
        form = ProfileForm(data={})
        self.assertTrue(form.is_valid(), "ProfileForm should be valid if profile_picture is optional")