from django.db import models
from django.db.models.base import Model
from bank.models import Bank
from bike.models import Bike
class Card(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  type = models.CharField(max_length=2, null=True)
  blance = models.BigIntegerField(null = True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Linking(models.Model):
  card = models.ForeignKey(Card, related_name="linking_card", on_delete=models.CASCADE) #must one to one
  bank = models.ForeignKey(Bank, related_name="linking_bank", on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
  card = models.IntegerField()
  bike = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)