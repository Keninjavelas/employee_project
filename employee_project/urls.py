from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('employees.urls')),  # dashboard + employees/departments API
    path('api/', include('employees.urls')),        # direct API access
    path('attendance/', include('attendance.urls')),
]
