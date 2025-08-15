from rest_framework import serializers
from .models import Employee, Department
from attendance.models import Attendance  # Removed Performance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Department.objects.all(),
        source='department'
    )
    department_name = serializers.CharField(
        source='department.name', 
        read_only=True
    )  # Added for charts and readability

    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            'email',
            'phone_number',
            'address',
            'date_of_joining',
            'department',
            'department_id',
            'department_name',  # Extra field for chart usage
            'is_active',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']
