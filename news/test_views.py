from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from news.models import Post, Comment, Category
from news.forms import ContactForm, CommentForm
from django.core.files.uploadedfile import SimpleUploadedFile


class TestViews(TestCase):

    def setUp(self):
        """Set up test data for the views."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.category = Category.objects.create(name="Test Category",
                                                slug="test-category")
        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=self.user,
            content="Test content",
            status=1
        )
        self.post.categories.add(self.category)
        self.contact_url = reverse('contact')
        self.post_detail_url = reverse('post-detail', args=[self.post.slug])

    def test_contact_view_get(self):
        """Test GET request for the Contact page."""
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contact_view_post_valid_data(self):
        """Test POST request for the Contact page with valid data."""
        response = self.client.post(self.contact_url, {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertRedirects(response, self.contact_url)

    def test_contact_view_post_invalid_data(self):
        """Test POST request for the Contact page with invalid data."""
        response = self.client.post(self.contact_url, {
            'name': '',
            'email': '',
            'subject': '',
            'message': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/contact.html')
        self.assertFalse(response.context['form'].is_valid())

    def test_post_detail_view_get(self):
        """Test GET request for a post detail page."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/post_detail.html')
        self.assertEqual(response.context['object'], self.post)
        self.assertIsInstance(response.context['form'], CommentForm)

    def test_post_detail_view_post_comment(self):
        """Test POST request to submit a comment."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.post_detail_url, {
            'body': 'This is a test comment'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.post_detail_url)
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.body, 'This is a test comment')
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.user, self.user)

    def test_post_list_view_get(self):
        """Test GET request for the post list view."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/index.html')
        self.assertIn(self.post, response.context['posts'])

    def test_category_post_list_view_get(self):
        """Test GET request for the category post list view."""
        response = self.client.get(reverse('category-posts',
                                           args=[self.category.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/index.html')
        self.assertIn(self.post, response.context['posts'])
