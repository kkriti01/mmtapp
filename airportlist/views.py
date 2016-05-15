import django_filters
from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework import filters


from .models import Airports
from .serializers import AirportSerializer


class AirportViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Airports.objects.all()
    serializer_class = AirportSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=code', '=name', '=country')


def index(request):
    return render(request, "index.html")

