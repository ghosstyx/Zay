from itertools import product

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from index.models import *
from index.serializers import *


class FeaturedProductViewSet(viewsets.ModelViewSet):
    queryset =FeaturedProducts.objects.all()
    serializer_class = FeaturedProductSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class CardBodiesViewSet(viewsets.ModelViewSet):
    queryset = CardBodies.objects.all()
    serializer_class = CardBodiesSerializer

def index(request):
    featured_products = FeaturedProducts.objects.all()
    categories = Categories.objects.all()
    context = {'featured_products': featured_products, 'categories': categories}
    return render(request, 'index.html', context=context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def shop(request):
    cardbodies = CardBodies.objects.all()
    context = {'cardbodies': cardbodies}
    return render(request, 'shop.html', context=context)


def shopsingle(request, id):
    cardbodies = CardBodies.objects.all()
    cardb = get_object_or_404(CardBodies, id=id)
    context = {'cardbodies': cardbodies, 'cardb': cardb}
    # print(cardb.albums.all())
    return render(request, 'shop-single.html', context=context)