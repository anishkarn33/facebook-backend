from django.db import models

# Create your models here.

class Newsfeed(models.Model):
    body = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=True)


class NewsfeedFile(models.Model):
    url = models.URLField(null=True, blank=True)
    newsfeed = models.ForeignKey(Newsfeed, on_delete=models.CASCADE, related_name='files')
    FILE_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('other', 'Other'),
    )
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES, default='image')

