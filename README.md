# Employee Management System

A Django-based application to manage employees, departments, and attendance with an integrated dashboard and REST API.

---

## 🚀 Features
- Full CRUD for Employees and Departments
- Attendance tracking with status options
- Dashboard with interactive charts (Chart.js)
- REST API endpoints using Django REST Framework.

---

## 🛠 Tech Stack
- **Backend:** Django, Django REST Framework  
- **Database:** SQLite (default) — can be replaced with PostgreSQL/MySQL  
- **Frontend:** Django Templates + Chart.js  
- **Version Control:** Git & GitHub  

---

## 📦 Installation & Setup

```bash
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/employee_project.git
cd employee_project

# 2️⃣ Create and activate a virtual environment
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run database migrations
python manage.py migrate

# 5️⃣ Create a superuser (for admin access)
python manage.py createsuperuser

# 6️⃣ Start the development server
python manage.py runserver

---

## Access the Application
Admin Panel: http://127.0.0.1:8000/admin/

Dashboard: http://127.0.0.1:8000/dashboard/

📡 API Endpoints
Endpoint	Description
/api/employees/	Manage employees
/api/departments/	Manage departments
/attendance/	View attendance records

This project is licensed under the MIT License.
