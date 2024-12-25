from rest_framework import serializers
from index.models import *

class FeaturedProductSerializer(serializers.ModelSerializer):
    class Meta:
      model = FeaturedProducts
      fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
      model = Categories
      fields = '__all__'

class CardBodiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardBodies
        fields = '__all__'