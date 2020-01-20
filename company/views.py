from .models import Company, CompanySerializer
from rest_framework import viewsets
from rest_framework import generics


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name_last')
    serializer_class = CompanySerializer

