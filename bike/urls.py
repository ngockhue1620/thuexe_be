from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *
router = SimpleRouter()
router.register('', BikeModelViewSet, 'bike')
router.register('/paking', PakingModelViewSet, 'paking')

urlpatterns = [
    path('', include(router.urls)),
]