
import random
import os
from django.db import models
from django.db.models import Q
from django.urls import reverse

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 3957568869)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )

class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

    def search(self, query):
        lookups = Q(title__icontains=query) | Q(description__icontains=query)| Q(price__icontains=query)|Q(tag__title__icontains=query)
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)


class Product(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, default='abc')
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default=False)

    objects = ProductManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)
        # return reverse("detail", kwargs={"slug":self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    @property
    def name(self):
        return self.title
