from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewset, UserRegistrationApiview, activate, UserloginApiView, UserlogoutApiview
router = DefaultRouter()
# Create a router and register our ViewSets with it.
router.register('list', PatientViewset) # Router banaici

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationApiview.as_view(), name='registration'),
    path('login/', UserloginApiView.as_view(), name='login'),
    path('logout/', UserlogoutApiview.as_view(), name='logout'),
    path('active/<uid64>/<token>/', activate, name="activate")
]
