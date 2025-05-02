from django.db import models

# Create your models here.
class Artwork(models.Model):
    STATUS_CHOICES = [
        ('In Exhibition', 'In Exhibition'),
        ('Sold', 'Sold'),
        ('Stored', 'Stored'),
    ]

    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    storage_location = models.CharField(max_length=200)

    def __str__(self):
        return self.title