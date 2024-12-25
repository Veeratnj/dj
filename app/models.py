from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)  # String field
    content = models.TextField()  # Text field for large text
    published_date = models.DateTimeField(null=True, blank=True)  # Date/Time
    author = models.CharField(max_length=100)  # Author name
    is_published = models.BooleanField(default=False)  # Boolean field

    def __str__(self):
        return self.title
