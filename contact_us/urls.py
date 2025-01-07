from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewset
router = DefaultRouter()
# Create a router and register our ViewSets with it.
router.register('', ContactViewset) # Router banaici

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
