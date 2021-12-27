from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework import status, viewsets
from django.db.models import Q
from bike.models import Bike
import datetime
from bike.serializer import BikeSeriallize
class CardModelViewSet(viewsets.ModelViewSet):
  queryset = Card.objects.all()
  serializer_class = CardSeriallize
  @action(methods=['post'], detail=False, url_path="thue")
  def thue(self, request):
    data = request.data 
    print(data)
    try:
      da_thue = Order.objects.filter(Q(card = data['card']) | Q(bike = data['bike']))
      print(da_thue)
      if len(da_thue) > 0:
        return Response({"mess": "Bạn chưa trả xe", "error": True}, status=status.HTTP_200_OK)
      
      card = Card.objects.get(pk=data['card'])
      if(card.blance < 1000000):
        return Response({"mess": "Tài khoản của bạn không đủ", "error": True})

      Order.objects.create(card=int(data['card']), bike=data['bike'])
      bike = Bike.objects.get(pk=data['bike'])
      bike.status = False
      bike.save()
      return Response({"mess": "Thành công", "error": False}, status=status.HTTP_200_OK)
    except Exception as e:
      print(e)
      return Response({"mess": "Card không tồn tại", "error": True})


  @action(methods=['get'], detail=False, url_path="tra")
  def tra(self, request):
    card = request.GET['card']
    bike = request.GET['bike']
    print(card,bike)
    try:
      da_thue = Order.objects.filter(card = card, bike = bike)
      if len(da_thue) == 0:
        return Response({"mess": "xe trả và mượn không trùng khớp", "error": True}, status=status.HTTP_200_OK)
      start_time = da_thue[0].created_at
      end_time = datetime.datetime.now()
      print("start_time",start_time.hour, start_time.minute  )
      print("end_time", end_time.hour, end_time.minute)
      card = Card.objects.get(pk=card)
      money = (int(end_time.hour) - (int(start_time.hour)+7))*60 + int(end_time.minute) - int(start_time.minute)
      print(money, card.blance)
      conlai = card.blance - money*2000
      card.blance = card.blance - conlai
      update_bike = Bike.objects.get(pk=bike)
      update_bike.status =True 
      update_bike.save()
      card.save()
      da_thue[0].delete()

      mess = "Thành công, tổng chi phí là:" + str(money*2000)
      print(mess)
      return Response({"mess": mess, "error": False}, status=status.HTTP_200_OK)
    except Exception as e:
      print(e)
      return Response({"mess": "Card không tồn tại", "error": True})

  @action(methods=['get'], detail=False, url_path="tim")
  def tim(self, request):
    card = request.GET['card']
    bike = request.GET['bike']
    try:
      da_thue = Order.objects.filter(card = card, bike = bike)
      if len(da_thue) == 0:
        return Response({"mess": "xe trả và mượn không trùng khớp", "error": True}, status=status.HTTP_200_OK)
      data= Bike.objects.get(pk=bike)
      serializer = BikeSeriallize(data)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      print(e)
      return Response({"mess": "Card không tồn tại", "error": True})