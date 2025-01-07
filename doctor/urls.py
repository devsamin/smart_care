from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter() # router anci
# Create a router and register our ViewSets with it.
router.register('spacialization', views.SerializationViewset) # Router banaici
router.register('designation', views.DesignationViewset) 
router.register('available_time', views.AvailableTimeViewset) 
router.register('list', views.DoctorViewset) 
router.register('reviews', views.ReviewViewset) 

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
