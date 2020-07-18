from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.contrib.auth.models import User


class User(AbstractUser):
    is_governmentEmployee = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    # MinistryName = models.ForeignKey(Ministry, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    Address = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)