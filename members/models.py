from django.db import models
from uuid import uuid4


def upload_picture(instance, filename):
    extension = filename.split('.')[-1]
    return 'static/uploads/members/{}.{}'.format(uuid4().hex, extension)


class Member(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255)
    github = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    picture = models.FileField(upload_to=upload_picture, null=True)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
