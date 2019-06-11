from rest_framework import serializers
from .models import Beer, Review


class BeerSerializer(serializers.ModelSerializer):
    """ Serielizer class to determine what JSON we want to get from the Beer model
    """
    class Meta:
        model = Beer
        fields = ('id', 'name', 'description', 'abv')


class ReviewSerializer(serializers.ModelSerializer):
    """ Serielizer class to determine what JSON we want to get from the Review model
    """
    class Meta:
        model = Review
        fields = ('id', 'beer', 'user', 'stars', 'comment')