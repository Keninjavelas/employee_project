from django.shortcuts import render
from employees.models import Employee, Department
from attendance.models import Attendance
from django.db.models import Count
from datetime import timedelta, date
from rest_framework import viewsets
from .serializers import EmployeeSerializer, DepartmentSerializer


# --------------------------
# DRF API ViewSets
# --------------------------
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# --------------------------
# Dashboard view (Performance removed)
# --------------------------
def dashboard(request):
    # Employees per department
    dept_data = Department.objects.annotate(emp_count=Count('employees'))
    dept_labels = [d.name for d in dept_data]
    dept_counts = [d.emp_count for d in dept_data]

    # Attendance trend for last 30 days
    today = date.today()
    last_30_days = [today - timedelta(days=i) for i in range(29, -1, -1)]
    attendance_labels = [d.strftime('%Y-%m-%d') for d in last_30_days]
    attendance_counts = [
        Attendance.objects.filter(date=d, status='present').count()
        for d in last_30_days
    ]

    dashboard_data = {
        "dept_labels": dept_labels,
        "dept_counts": dept_counts,
        "attendance_labels": attendance_labels,
        "attendance_counts": attendance_counts,
    }

    return render(request, 'dashboard.html', {'dashboard_data': dashboard_data})
