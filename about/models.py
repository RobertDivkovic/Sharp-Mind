from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


class CollaborationRequest(models.Model):
    """
    Represents a collaboration request submitted by a user.

    Fields:
        name (CharField): The full name of the person submitting the request.
        email (EmailField): The email address of the submitter.
        message (TextField): The message or
        content of the collaboration request.
        created_on (DateTimeField): Timestamp when the request was created.
        user (ForeignKey): The user associated
        with the request, if authenticated.

    Meta:
        ordering: Orders collaboration requests
        by creation date in descending order.

    Methods:
        __str__: Returns a human-readable
        representation of the collaboration request.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='collaboration_requests',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string representation of the collaboration request.

        Example:
            "Request by John Doe on 2025-01-23 12:00:00"
        """
        return f"Request by {self.name} on {self.created_on}"


class About(models.Model):
    """
    Represents the About section of the website.

    Fields:
        title (CharField): The title of the About section.
        content (TextField): The content or
        description for the About section.
        profile_image (CloudinaryField): An image
        associated with the About section.

    Methods:
        __str__: Returns the title of
        the About section as its string representation.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        """
        Returns a string representation of the About instance.

        Example:
            "About Sharp-Mind"
        """
        return self.title
