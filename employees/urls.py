from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, dashboard

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  # Charts/dashboard view
    path('', include(router.urls)),  # API routes (employees/, departments/)
]
