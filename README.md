# Event Management & Resource Allocation Web App

##  Overview
This is a **Flask-based Event & Resource Management Web App** that allows users to manage events, resources, and allocations.  
It includes **CRUD functionalities**, conflict-free scheduling, clean UI, and a simple reporting system.

This project is ideal for **college submissions, internships, resumes, and portfolio projects**.

---

## ⭐ Features

### 🗓️ Event Management
- Add, view, update, and delete events  
- Display allocated resources for each event  
- Organized event table with centered alignment  

### 🧰 Resource Management
- Add resources (Lab, Room, Projector, Instructor, etc.)  
- Update and delete resources  
- View all resources  

### 🔗 Resource Allocation
- Allocate resource to an event  
- Smart conflict prevention  
- Edit or remove allocations  
- List all allocations  

### 📊 Reports
- Resource utilization summary  
- Total hours used  
- Upcoming bookings  

### 🎨 UI / Frontend
- Clean HTML interface  
- Custom CSS (no Bootstrap)  
- Background image & modern homepage UI  

---

## 🛠 Tech Stack


-Frontend: **HTML, CSS 
-Backend :**Flask (Python) 
-Database : **MySQL 

## 📋 Prerequisites

Install:

- Python 3.10+
- MySQL Server
- pip (for installing Python packages)

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
### Running the App

1. Run the Flask app:

python app.py
Visit http://127.0.0.1:5000/ in your browser to start using the app.

Application Structure
app.py: Main Flask application file.

templates/: Directory containing HTML templates.

home.html: Home page of the app.
events.html: Page for managing events.
add_event.html: Page for adding new events.
edit_event.html: Page for editing existing events.
resources.html: Page for managing resources.
add_resource.html: Page for adding new resources.
edit_resource.html: Page for updating resources.
allocate.html: Page for allocating resources.
edit_allocation.html: Page for editing allocations.
report.html: Page showing resource utilization reports.
static/: Directory containing static files like CSS and images.

###Event Management
Add Event: Add new events with title, description, start time, and end time.
Update Event: Edit details of an existing event.
View Events: View all created events with allocated resources.
Delete Event: Remove any event.
<img width="1907" height="1014" alt="View event" src="https://github.com/user-attachments/assets/d23c11bd-a5c7-4400-ba67-f76e361e6e48" />


###Resource Management
Add Resource: Add new resources (labs, rooms, projectors, instructors…)
Update Resource: Edit existing resource details.
View Resources: View all resources.
Delete Resource: Remove a resource after clearing allocations.
<img width="1919" height="1021" alt="view source" src="https://github.com/user-attachments/assets/096ab5d3-3a7a-4459-affa-ccb546f58e0d" />


###Resource Allocation
Add Allocation: Allocate a resource to an event.
Conflict Detection: Prevents overlapping bookings.
Update Allocation: Change allocated resource or event.
View Allocations: View all event-resource allocations.
<img width="1911" height="964" alt="allocate resouce" src="https://github.com/user-attachments/assets/c32df648-3b2d-4ea2-905b-0ed37838b9fb" />



###Report
Shows total usage duration of each resource.
Displays upcoming bookings.
Helps identify most-used resources.
<img width="1891" height="1029" alt="Final report" src="https://github.com/user-attachments/assets/91314623-44d5-4534-9f21-3824fa371b18" />



>>>>>Future Improvements
JWT Authentication: Implement secure login system for admin and staff.
Role-based Access Control (RBAC): Different permissions based on roles.
Advanced Reports: Weekly, monthly, and yearly analytics.
Calendar View: Event scheduling using a calendar interface.
Export to Excel/PDF: Export reports and event data.

###License
This project is licensed under the MIT License - see the LICENSE file for details.



