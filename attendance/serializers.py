from rest_framework import serializers
from attendance.models import Attendance
from employees.serializers import EmployeeSerializer
from employees.models import Employee
import calendar  # ✅ To convert month numbers to names


class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Employee.objects.all(),
        source='employee'
    )
    month = serializers.SerializerMethodField()  # ✅ Added field for month name

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'employee_id', 'date', 'status', 'month']

    def get_month(self, obj):
        """Return month name for the attendance date."""
        return calendar.month_name[obj.date.month] if obj.date else None
