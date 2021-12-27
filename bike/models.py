from django.db import models

class Paking(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)

class Bike(models.Model):
  name = models.CharField(max_length=255)
  paking = models.ForeignKey(Paking, related_name="paking", on_delete=models.SET_NULL, null=True, blank=True)
  bike_code = models.CharField(max_length=255)
  status = models.BooleanField()
  image = models.TextField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
