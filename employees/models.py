from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    date_of_joining = models.DateField()
    department = models.ForeignKey(
        Department,
        related_name='employees',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


class Performance(models.Model):
    employee = models.ForeignKey(
        Employee,
        related_name='employee_performances',  # renamed to avoid clashes with attendance app
        on_delete=models.CASCADE
    )
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee.name} - {self.rating} on {self.date}"
