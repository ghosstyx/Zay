from django.urls import path, include
from rest_framework.routers import DefaultRouter, Route
from django.urls import path
from index.views import *
from . import views


router = DefaultRouter()
router.register('FeaturedProduct', FeaturedProductViewSet, basename='featured-product')
router.register('Categories', CategoriesViewSet, basename='categories')
router.register('CardBodies', CardBodiesViewSet, basename='card-bodies')

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('shopsingle/<int:id>/', views.shopsingle, name='shop-single'),
    path('api/', include(router.urls)),
]
