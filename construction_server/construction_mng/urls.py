from django.urls import path, include
from rest_framework.routers import DefaultRouter
from construction_mng import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api/workers', views.WorkerViewSet, basename="a")
router.register(r'api/activities', views.ActivityViewSet, basename='b')
router.register(r'api/emergencies', views.EmergencyViewSet, basename='c')
router.register(r'api/attendances', views.AttendanceViewSet, basename='d')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/attendances/overtime/', views.AttendanceViewSet.as_view({'get': 'overtime'})),
]