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

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
  list_display = ['photo', 'photo_caption', 'cardbody']

@admin.register(CardBodies)
class CardBodiesAdmin(admin.ModelAdmin):
  inlines = [AlbumInline]
  list_display = ['title', 'sizes', 'price', 'date']
  search_fields = ['title']
  list_filter = ['date']


