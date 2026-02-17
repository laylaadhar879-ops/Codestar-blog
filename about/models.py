from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Stores a single about page entry with the title, profile image, and content.
    """
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request entry with the name, email, and message of the requester.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.name} ({self.email})"

