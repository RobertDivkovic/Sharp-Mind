from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    STATUS = ((0, "Draft"), (1, "Published"))

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_posts")
    featured_image = CloudinaryField('image', default='placeholder')  # Add Cloudinary field for featured images
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    upvotes = models.ManyToManyField(User, related_name="upvoted_posts", blank=True)
    downvotes = models.ManyToManyField(User, related_name="downvoted_posts", blank=True)
    categories = models.ManyToManyField(Category, related_name="posts", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def total_upvotes(self):
        return self.upvotes.count()

    def total_downvotes(self):
        return self.downvotes.count()

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.CharField(max_length=80)  # Legacy field for backward compatibility
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)  # Track updates
    approved = models.BooleanField(default=False)
    email = models.EmailField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments", null=True, blank=True,
    )  # Associate with user

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        # Use the associated user if available; otherwise, fallback to the `author` field
        if self.user:
            return f"Comment by {self.user.username} on {self.post}"
        return f"Comment by {self.author} on {self.post}"

class Vote(models.Model):
    VOTE_CHOICES = (
        (1, "Upvote"),
        (-1, "Downvote"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes")
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="votes")
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # A user can vote only once per post