from django.urls import path, include
from rest_framework.routers import DefaultRouter
from construction_mng import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'workers', views.WorkerViewSet, basename="a")
router.register(r'activities', views.ActivityViewSet, basename='b')
router.register(r'emergencies', views.EmergencyViewSet, basename='c')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]