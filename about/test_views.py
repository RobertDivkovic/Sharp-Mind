from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from about.models import About, CollaborationRequest
from about.forms import CollaborationRequestForm


class TestAboutViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser",
                                             password="password")
        self.client.login(username="testuser", password="password")
        self.about = About.objects.create(title="About Us",
                                          content="Details about us.")
        self.about_url = reverse('about')
        self.collaboration_request_url = reverse('collaboration_request')
        self.collaboration_request_update_url = reverse(
            'collaboration_request_update', args=[1])
        self.collaboration_request_delete_url = reverse(
            'collaboration_request_delete', args=[1])

    def test_about_page_view_get(self):
        """Test GET request for the About page."""
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
        self.assertEqual(response.context['about'], self.about)

    def test_about_page_view_authenticated_user(self):
        """Test About page for authenticated users with collaboration form."""
        response = self.client.get(self.about_url)

        # Ensure the request is successful
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'about/about.html')

        # Verify the About content
        self.assertContains(response, "About Us")
        self.assertContains(response, "Details about us.")

        # Verify the CollaborationRequestForm is in the context
        self.assertIn('collaboration_form', response.context)
        self.assertIsInstance(response.context['collaboration_form'],
                              CollaborationRequestForm)

    def test_collaboration_request_view_get(self):
        """Test GET request for the Collaboration Request page."""
        response = self.client.get(self.collaboration_request_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/collaboration_request.html')

    def test_collaboration_request_view_post_valid(self):
        """Test POST request for Collaboration Request with valid data."""
        response = self.client.post(self.collaboration_request_url, {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test collaboration request.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.about_url)
        self.assertEqual(CollaborationRequest.objects.count(), 1)
        collaboration_request = CollaborationRequest.objects.first()
        self.assertEqual(collaboration_request.name, 'Test User')
        self.assertEqual(collaboration_request.user, self.user)

    def test_collaboration_request_view_post_invalid(self):
        """Test POST request for Collaboration Request with invalid data."""
        response = self.client.post(self.collaboration_request_url, {
            'name': '',
            'email': '',
            'message': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/collaboration_request.html')
        self.assertFalse(response.context['form'].is_valid())

    def test_collaboration_request_update_view(self):
        """Test CollaborationRequestUpdateView."""
        collaboration_request = CollaborationRequest.objects.create(
            user=self.user,
            name="Old Name",
            email="oldemail@example.com",
            message="Old message"
        )
        response = self.client.post(reverse('collaboration_request_update',
                                    args=[collaboration_request.id]), {
            'name': 'Updated Name',
            'email': 'updatedemail@example.com',
            'message': 'Updated message'
        })
        self.assertEqual(response.status_code, 302)
        collaboration_request.refresh_from_db()
        self.assertEqual(collaboration_request.name, 'Updated Name')
        self.assertEqual(collaboration_request.email,
                         'updatedemail@example.com')

    def test_collaboration_request_delete_view(self):
        """Test CollaborationRequestDeleteView."""
        collaboration_request = CollaborationRequest.objects.create(
            user=self.user,
            name="Test Name",
            email="testemail@example.com",
            message="Test message"
        )
        response = self.client.post(reverse('collaboration_request_delete',
                                    args=[collaboration_request.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CollaborationRequest.objects.filter
                         (id=collaboration_request.id).exists())
