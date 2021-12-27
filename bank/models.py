from django.db import models

class Bank(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
class Customer(models.Model):
  bank =models.ForeignKey(Bank, related_name='customer', on_delete=models.CASCADE, null=True)
  name = models.CharField(max_length=255)
  user_name = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  balance = models.BigIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)