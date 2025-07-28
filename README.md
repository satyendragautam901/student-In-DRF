# 🎓 Student CRUD API with Django REST Framework

This project is a **practice-based implementation** of **CRUD operations** (Create, Read, Update, Delete) on a `Student` table using **Django REST Framework (DRF)**.

> 🔧 Built for learning and experimenting with Django REST APIs.

---

## 🚀 Features

- ✅ Create a student entry
- 📥 Retrieve all or a single student
- ✏️ Update student information
- ❌ Delete a student record
- 🛠️ Admin interface to manage student data
- 📦 JSON-based API responses

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Django 4.2.x**
- **Django REST Framework**
- **SQLite** (default DB)
- **Postman** or **cURL** (for testing)

---

## 🔗 API Endpoints

| Method | Endpoint           | Description              |
|--------|--------------------|--------------------------|
| GET    | `/api/students/`   | Get all students         |
| GET    | `/api/students/<id>/` | Get single student      |
| POST   | `/api/students/`   | Create a new student     |
| PUT    | `/api/students/<id>/` | Update existing student |
| DELETE | `/api/students/<id>/` | Delete a student        |

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/student-In-DRF.git
cd student-In-DRF

# (Optional) Create a virtual environment
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
