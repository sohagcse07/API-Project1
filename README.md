# 🏢 Company & Employee API (Django REST Framework)

A Django REST Framework (DRF) based API to manage companies and their employees. Includes a custom endpoint to retrieve all employees under a specific company.

---

## 📁 Project Structure

project_root/
│
├── apiAPP/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py
│
├── templates/
│ └── home.html
│
├── manage.py
├── requirements.txt
└── README.md


---

## ⚙️ Technologies Used

- Python 3.x 🐍
- Django 🧩
- Django REST Framework 🌐
- SQLite3 (default DB)
- HTML (Template rendering)

---

## 🚀 Features

- ✅ CRUD operations for **Company** model
- ✅ CRUD operations for **Employee** model
- ✅ Custom nested endpoint: `/company/{id}/employess/`
- ✅ Browsable API using DRF
- ✅ Simple HTML-rendered homepage (`home.html`)

---

## 🏁 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

## 2️⃣ Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate        # Linux / Mac
venv\Scripts\activate           # Windows

### 3️⃣ Install Required Packages
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the Development Server
python manage.py runserver


🌐 Company API

| Method | Endpoint                   | Description                          |
| ------ | -------------------------- | ------------------------------------ |
| GET    | `/company/`                | List all companies                   |
| POST   | `/company/`                | Create a new company                 |
| GET    | `/company/{id}/`           | Retrieve a company by ID             |
| PUT    | `/company/{id}/`           | Update a company by ID               |
| DELETE | `/company/{id}/`           | Delete a company by ID               |
| GET    | `/company/{id}/employess/` | Get all employees under that company |


👨‍💼 Employee API
| Method | Endpoint         | Description                |
| ------ | ---------------- | -------------------------- |
| GET    | `/employe/`      | List all employees         |
| POST   | `/employe/`      | Create a new employee      |
| GET    | `/employe/{id}/` | Retrieve an employee by ID |
| PUT    | `/employe/{id}/` | Update an employee by ID   |
| DELETE | `/employe/{id}/` | Delete an employee by ID   |


👤 Author

> Name: Sohag Hossain

> Institute: Brahmanbaria Polytechnic Institute (CST)

> GitHub: @sohagcse07