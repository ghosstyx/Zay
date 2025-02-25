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
    date = models.DateField(verbose_name="Date")
    brand = models.CharField(max_length=255, verbose_name="Brand")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Card Body"
        verbose_name_plural = "Card Bodies"

class Album(models.Model):
    photo = models.FileField(upload_to="albums/", verbose_name="Photo")
    photo_caption = models.TextField(verbose_name="Photo Caption")
    photo_id = models.IntegerField(auto_created=True, verbose_name="Photo ID")
    cardbody = models.ForeignKey(CardBodies, on_delete=models.CASCADE, related_name="albums")

    def __str__(self):
        return self.photo_caption

    class Meta:
        ordering = ['photo_id']

class ColorChoice(models.Model):
    color = models.CharField(max_length=255, verbose_name="Color")
    price = models.FloatField(verbose_name="Price")
    color_id = models.IntegerField(auto_created=True,verbose_name="Color ID")
    cardbody = models.ForeignKey(CardBodies, on_delete=models.CASCADE, related_name="color")

    def __str__(self):
        return self.color

    class Meta:
        ordering = ['color_id']

class AvailableColors(models.Model):
    color = models.CharField(max_length=255, verbose_name="Color")
    color_id = models.IntegerField(auto_created=True,verbose_name="Color ID")
    cardbody = models.ForeignKey(CardBodies, on_delete=models.CASCADE, related_name="colors")
    def __str__(self):
        return self.color
    class Meta:
        ordering = ['color_id']
