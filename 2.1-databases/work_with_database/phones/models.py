from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    price = models.IntegerField()
    image = models.URLField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=10)
    slug = models.SlugField(max_length=255, unique=True)

    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)
