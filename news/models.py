from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.


class Category(models.Model):
    """
    Represents a category for grouping posts.

    Attributes:
        name (str): The name of the category.
        slug (str): A URL-friendly identifier for the category.
    """

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        """
        Returns the string representation of the category name.
        """
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (str): The title of the post.
        slug (str): A URL-friendly identifier for the post.
        author (User): The author of the post.
        featured_image (CloudinaryField): An image associated with the post.
        updated_on (datetime): The last time the post was updated.
        content (str): The main content of the post.
        created_on (datetime): When the post was created.
        status (int): The status of the post (draft or published).
        excerpt (str): A short summary of the post.
        upvotes (ManyToManyField): Users who upvoted the post.
        downvotes (ManyToManyField): Users who downvoted the post.
        categories (ManyToManyField): Categories associated with the post.
    """
    STATUS = ((0, "Draft"), (1, "Published"))

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="news_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    upvotes = models.ManyToManyField(User, related_name="upvoted_posts",
                                     blank=True)
    downvotes = models.ManyToManyField(User, related_name="downvoted_posts",
                                       blank=True)
    categories = models.ManyToManyField(Category, related_name="posts",
                                        blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns the string representation of the post title.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL for the post's detail page.
        """
        return f'/{self.slug}/'

    def total_upvotes(self):
        """
        Returns the total number of upvotes for the post.
        """
        return self.upvotes.count()

    def total_downvotes(self):
        """
        Returns the total number of downvotes for the post.
        """
        return self.downvotes.count()

    def calculate_trending_score(self):
        """
        Calculates the trending score for the post.
        Trending score is based on the number of upvotes and comments
        within the last 7 days.
        """
        recent_period = now() - timedelta(days=7)
        if self.created_on < recent_period:
            return 0

        upvote_score = self.upvotes.count() * 2  # Upvotes have double weight
        comment_score = self.comments.count()  # One point per comment
        return upvote_score + comment_score


class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Attributes:
        post (Post): The post the comment is associated with.
        author (str): The name of the comment's author.
        body (str): The content of the comment.
        created_on (datetime): When the comment was created.
        updated_on (datetime): When the comment was last updated.
        approved (bool): Whether the comment is approved for display.
        email (str): Email address of the commenter.
        user (User): The associated user (if logged in).
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    email = models.EmailField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments",
        null=True, blank=True,
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns the string representation of the comment.
        Includes the author and the associated post.
        """
        if self.user:
            return f"Comment by {self.user.username} on {self.post}"
        return f"Comment by {self.author} on {self.post}"


class Vote(models.Model):
    """
    Represents a vote (upvote or downvote) on a post.

    Attributes:
        user (User): The user who cast the vote.
        post (Post): The post being voted on.
        vote (int): The vote type (1 for upvote, -1 for downvote).
        created_on (datetime): When the vote was cast.
    """
    VOTE_CHOICES = (
        (1, "Upvote"),
        (-1, "Downvote"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="votes")
    post = models.ForeignKey('Post', on_delete=models.CASCADE,
                             related_name="votes")
    vote = models.SmallIntegerField(choices=VOTE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')


class ContactSubmission(models.Model):
    """
    Represents a contact form submission.

    Attributes:
        name (str): The name of the person submitting the form.
        email (str): The email address of the submitter.
        subject (str): The subject of the message.
        message (str): The message content.
        created_on (datetime): When the submission was created.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a summary of the contact submission.
        """
        return f"Message from {self.name} on {self.created_on:%Y-%m-%d}"


class Profile(models.Model):
    """
    Represents a user profile with additional attributes.

    Attributes:
        user (User): The user associated with this profile.
        profile_picture (CloudinaryField): The user's profile picture.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    profile_picture = CloudinaryField('image', default='placeholder',
                                      blank=True)

    def __str__(self):
        """
        Returns the string representation of the user's profile.
        """
        return f"{self.user.username}'s Profile"
