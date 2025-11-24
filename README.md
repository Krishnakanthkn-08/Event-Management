# 🎯 Event Management & Resource Allocation Web App

## 📌 Overview
This is a **Flask-based Event & Resource Management Web App** that allows users to manage events, resources, and allocations.  
It includes **CRUD functionalities**, conflict-free scheduling, clean UI, and a simple reporting system.

This project is ideal for **college submissions, internships, resumes, and portfolio projects**.

---

## ⭐ Features

### 🗓️ Event Management
- Add, view, update, and delete events  
- Display allocated resources for each event  
- Clean and centered event table  

### 🧰 Resource Management
- Add resources (Lab, Room, Projector, Instructor, etc.)  
- Update and delete resources  
- View all resources  

### 🔗 Resource Allocation
- Allocate resource to an event  
- Smart conflict detection  
- Edit or remove allocations  
- View all allocations  

### 📊 Reports
- Resource utilization summary  
- Total hours used  
- Upcoming bookings  

### 🎨 UI / Frontend
- Simple HTML pages  
- Custom CSS (no Bootstrap)  
- Background image & professional home page  

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS  
- **Backend:** Flask (Python)  
- **Database:** MySQL  

---

## 📋 Prerequisites

Install:

- Python 3.10+  
- MySQL Server  
- pip  

---

## 📦 Installation

### 1️⃣ Clone the Repository

git clone https://github.com/Krishnakanthkn-08/Event-Management
cd Event-Management
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Create MySQL Database
sql
Copy code
CREATE DATABASE event_system;
4️⃣ Configure DB Connection
In db.py:

python
Copy code
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="event_system"
)
▶️ Running the App
Start Flask:

bash
Copy code
python app.py
Visit:

👉 http://127.0.0.1:5000/

📁 Application Structure
app.py: Main Flask application file

templates/ — HTML templates

home.html

events.html

add_event.html

edit_event.html

resources.html

add_resource.html

edit_resource.html

allocate.html

edit_allocation.html

report.html

static/ — CSS and images

🗓️ Event Management
Add Event
Update Event
View Events
Delete Event
Screenshot:
<img width="1907" height="1014" alt="View event" src="https://github.com/user-attachments/assets/d23c11bd-a5c7-4400-ba67-f76e361e6e48" />

🧰 Resource Management
Add Resource
Edit Resource
View Resources
Delete Resource
Screenshot:
<img width="1919" height="1021" alt="view source" src="https://github.com/user-attachments/assets/096ab5d3-3a7a-4459-affa-ccb546f58e0d" />

🔗 Resource Allocation
Add Allocation
Conflict Detection
Edit Allocation
View All Allocations
Screenshot:
<img width="1911" height="964" alt="allocate resouce" src="https://github.com/user-attachments/assets/c32df648-3b2d-4ea2-905b-0ed37838b9fb" />

📊 Report
Shows total usage duration
Displays upcoming bookings
Helps identify most-used resources
Screenshot:
<img width="1891" height="1029" alt="Final report" src="https://github.com/user-attachments/assets/91314623-44d5-4534-9f21-3824fa371b18" />

🚀 Future Improvements
JWT Authentication
Admin & Staff Roles (RBAC)
Advanced Reports
Calendar View Scheduling
Export to PDF / Excel
📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

yaml
Copy code
