from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet  # ✅ Removed PerformanceViewSet

router = DefaultRouter()
router.register(r'attendance', AttendanceViewSet)  # ✅ Only Attendance

urlpatterns = [
    path('', include(router.urls)),
]
