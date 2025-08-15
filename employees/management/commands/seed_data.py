# employees/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Employee, Department
from attendance.models import Attendance, Performance

class Command(BaseCommand):
    help = "Idempotent seeding: adds missing employees, attendance, and performance without duplicates."

    def handle(self, *args, **kwargs):
        fake = Faker()

        # 1️⃣ Create or get departments
        departments = ['HR', 'IT', 'Finance', 'Marketing']
        dept_objs = []
        for d in departments:
            dept_obj, _ = Department.objects.get_or_create(name=d)
            dept_objs.append(dept_obj)

        # 2️⃣ Create or get employees
        for _ in range(30):
            email = fake.unique.email()
            emp, created = Employee.objects.get_or_create(
                email=email,
                defaults={
                    'name': fake.name(),
                    'phone_number': fake.phone_number(),
                    'address': fake.address(),
                    'date_of_joining': fake.date_between(start_date='-2y', end_date='today'),
                    'department': random.choice(dept_objs)
                }
            )

            # 3️⃣ Attendance (add only missing dates)
            attendance_dates = set()
            while len(attendance_dates) < 5:
                attendance_dates.add(fake.date_between(start_date='-30d', end_date='today'))

            for att_date in attendance_dates:
                Attendance.objects.get_or_create(
                    employee=emp,
                    date=att_date,
                    defaults={'status': random.choice(['P', 'A', 'L'])}
                )

            # 4️⃣ Performance (add only missing review dates)
            for _ in range(2):
                review_date = fake.date_between(start_date='-1y', end_date='today')
                Performance.objects.get_or_create(
                    employee=emp,
                    review_date=review_date,
                    defaults={
                        'rating': random.randint(1, 5),
                        'review': fake.sentence(nb_words=10)
                    }
                )

        self.stdout.write(self.style.SUCCESS("Database seeded idempotently!"))
