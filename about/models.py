from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

class CollaborationRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collaboration_requests', null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Request by {self.name} on {self.created_on}"

class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')  # Cloudinary field for the profile image

    def __str__(self):
        return self.title