from rest_framework import serializers
from .models import Categories,Companies

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields='__all__'

class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = '__all__'


class UserInputSerializer(serializers.Serializer):
    top=serializers.IntegerField()
    minPrice = serializers.IntegerField()
    maxPrice = serializers.IntegerField()
