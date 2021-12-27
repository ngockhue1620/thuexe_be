
from rest_framework import serializers
from .models import *

class CardSeriallize(serializers.ModelSerializer):
  class Meta: 
    fields = '__all__'
    model = Card

