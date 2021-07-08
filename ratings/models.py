from django.db import models
from django.conf import settings

# Create your models here.


class Beer(models.Model):
    name = models.CharField(max_length=255)


class Review(models.Model):
    beer = models.ForeignKey(
        'Beer', on_delete=models.CASCADE, related_name='reviews')

    # star ratings
    STAR_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    stars = models.PositiveSmallIntegerField(choices=STAR_CHOICES, default=3)

    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
