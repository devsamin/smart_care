from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewset
router = DefaultRouter()
# Create a router and register our ViewSets with it.
router.register('list', ServiceViewset) # Router banaici

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
