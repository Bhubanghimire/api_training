from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=10)


class Product(models.Model):
    name = models.CharField(max_length=50)
    product_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    price = models.IntegerField()
    cover_file = models.ImageField()
    keywords = models.ManyToManyField(Keyword)
    added_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name




    