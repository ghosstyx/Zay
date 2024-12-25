from django.db import models

# Create your models here.

class FeaturedProducts(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    price = models.FloatField(verbose_name="Price")
    photo = models.FileField(upload_to="products/", verbose_name="Photo")

    class Meta:
        verbose_name = "Featured Product"
        verbose_name_plural = "Featured Products"

class Categories(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    photo = models.FileField(upload_to="categories/", verbose_name="Photo")
    date = models.DateField(verbose_name="Date")

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Categories"

class CardBodies(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    sizes = models.CharField(max_length=255, verbose_name="Sizes")
    price = models.FloatField(verbose_name="Price")
    photo = models.FileField(upload_to="cards/", verbose_name="Photo")
    date = models.DateField(verbose_name="Date")
    

    class Meta:
        verbose_name = "Card Body"
        verbose_name_plural = "Card Bodies"