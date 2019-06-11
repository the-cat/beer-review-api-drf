from django.shortcuts import render
from rest_framework import viewsets

from .models import Beer, Review
from .serializers import BeerSerializer, ReviewSerializer


class BeerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Beer.objects.all().order_by('name')
    serializer_class = BeerSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
