from django.db.models import fields
from rest_framework import serializers
from .models import *

class BikeSeriallize(serializers.ModelSerializer):
  class Meta: 
    fields = '__all__'
    model = Bike
  
class PakingSerializer(serializers.ModelSerializer):
  paking = BikeSeriallize(many=True)
  class Meta:
    fields = ['name', 'address', 'paking']
    model = Paking