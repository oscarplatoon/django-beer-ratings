from django.db import models
from django.db.models.deletion import CASCADE

class Beer(models.Model):
    beer_brewer = models.CharField(max_length=200)
    beer_name = models.CharField(max_length=64)
    beer_type = models.CharField(max_length=64)

    def __str__(self):
        return f"Brewer: {self.beer_brewer}, Name: {self.beer_name}, Type: {self.beer_type}"

class Review(models.Model):
    beer = models.ForeignKey(Beer, on_delete=CASCADE, related_name="reviews")
    review = models.TextField()
