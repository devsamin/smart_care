from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # wifi banalam

router.register('', views.AppointmentViewset) # Entina delam

urlpatterns = [
    path('', include(router.urls))
]


