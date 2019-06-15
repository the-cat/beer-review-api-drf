from rest_framework import serializers
from .models import Beer, Review


class BeerSerializer(serializers.ModelSerializer):
    """ Serielizer class to determine what JSON we want to get from the Beer model
    """
    reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = Beer
        fields = ('id', 'name', 'description', 'abv', 'reviews')


class ReviewSerializer(serializers.ModelSerializer):
    """ Serielizer class to determine what JSON we want to get from the Review model
    """
    beer = serializers.CharField()
    user = serializers.CharField()
    class Meta:
        model = Review
        fields = ('id', 'beer', 'user', 'stars', 'comment')