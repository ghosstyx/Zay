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

@admin.register(CardBodies)
class CardBodiesAdmin(admin.ModelAdmin):
  list_display = ['title', 'sizes', 'price', 'photo', 'date']
  search_fields = ['title']
  list_filter = ['date']
