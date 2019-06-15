from django.shortcuts import render
from rest_framework import viewsets

from .models import Beer, Review
from .serializers import BeerSerializer, ReviewSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BeerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Beer.objects.all().order_by('name')
    serializer_class = BeerSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminUser,]
        return super(self.__class__, self).get_permissions()


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
