
from rest_framework import generics
from .models import Farmer
from .serializers import FarmerSerializer
from django_filters import rest_framework as filters

class FarmerFilter(filters.FilterSet):
    class Meta:
        model = Farmer
        fields = {
            'name': ['icontains']
        }

class FarmerListView(generics.ListAPIView):
    serializer_class = FarmerSerializer
    queryset = Farmer.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FarmerFilter
# Create your views here.
