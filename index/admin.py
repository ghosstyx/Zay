from PIL.ImageEnhance import Color
from django.contrib import admin
from index.models import *
# Register your models here.

@admin.register(FeaturedProducts)
class FeaturedProductsAdmin(admin.ModelAdmin):
  list_display = ['title', 'description', 'price', 'photo']
  search_fields = ['title', 'description']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
  list_display = ['title', 'photo', 'date']
  search_fields = ['title']
  list_filter = ['date']

class AlbumInline(admin.TabularInline):
  model = Album
  extra = 1

class ColorInline(admin.TabularInline):
  model = Color
  extra = 1

class AvailableColorsInline(admin.TabularInline):
  model = AvailableColors
  extra = 1

@admin.register(AvailableColors)
class AvailableColorsAdmin(admin.ModelAdmin):
  list_display = ['color', 'cardbody']
  list_filter = ['color_id']

@admin.register(ColorChoice)
class ColorChoiceAdmin(admin.ModelAdmin):
  list_display = ['color', 'price', 'cardbody']
  list_filter = ['color_id']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
  list_display = ['photo', 'photo_caption', 'cardbody']
  list_filter = ['photo_id']

@admin.register(CardBodies)
class CardBodiesAdmin(admin.ModelAdmin):
  inlines = [AlbumInline]
  list_display = ['title', 'sizes', 'price', 'date', 'brand']
  search_fields = ['title']
  list_filter = ['date']



