import imp
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import Advocate,Company
from .serializers import CompanySerializer,AdvocateSerializer
# Create your views here.

class AdvocateListAPIView(viewsets.ModelViewSet):
    lookup_field = 'username'
    serializer_class = AdvocateSerializer
    pagination_class = PageNumberPagination
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Advocate.objects.all().order_by('id')
        param = self.request.GET.get('query',None)
        if param is not None:
            queryset = Advocate.objects.filter(username__iexact=param) 
        return queryset

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        page = self.paginate_queryset(instance)
        serializer = AdvocateSerializer(page,many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)


class CompanyListAPIView(viewsets.ModelViewSet):    
    serializer_class = CompanySerializer
    pagination_class = PageNumberPagination
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Company.objects.all().order_by('id')
        param = self.request.GET.get('query',None)

        if param is not None:
            queryset = Company.objects.filter(name__iexact = param)

        return queryset

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        page = self.paginate_queryset(instance)
        serializer = self.get_serializer(page,many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)
