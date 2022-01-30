from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    git_hub_url = models.URLField(blank=True, null=True)

