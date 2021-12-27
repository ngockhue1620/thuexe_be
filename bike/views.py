
from django.shortcuts import render
from rest_framework import viewsets, status
from .models import*
from .serializer import *
from rest_framework.response import Response

class BikeModelViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSeriallize

class PakingModelViewSet(viewsets.ModelViewSet):
    queryset = Paking.objects.all()
    serializer_class = PakingSerializer

    def list(self, request):
        data = Paking.objects.all()
        serializer = PakingSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)