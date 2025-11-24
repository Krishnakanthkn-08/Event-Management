# 🎯 Event Management & Resource Allocation Web App

## 📌 Overview
This is a **Flask-based Event & Resource Management Web App** that allows users to manage events, resources, and allocations.  
It includes **CRUD functionalities**, conflict-free scheduling, clean UI, and a simple reporting system.

This project is ideal for **college submissions, internships, resumes, and portfolio projects**.

---

## ⭐ Features
## 🖼 Screenshots

### 🏠 Home Page
![Home Screenshot]()

### 📅 Events Page
![Events Screenshot]()

### 🧰 Resources Page
![Resources Screenshot](/mnt/data/4f4708eb-a876-47f9-b79f-aedc910b6935.png)

### 🔗 Allocation Page
![Allocation Screenshot](/mnt/data/4f4708eb-a876-47f9-b79f-aedc910b6935.png)

### 📊 Report Page
![Report Screenshot](/mnt/data/4f4708eb-a876-47f9-b79f-aedc910b6935.png)


### 🗓️ Event Management
- Add, view, update, and delete events  
- Display allocated resources for each event  
- Organized event table with centered alignment
-  

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

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS |
| Backend | Flask (Python) |
| Database | MySQL |
| Template Engine | Jinja2 |

---

## 📋 Prerequisites

Install:

- Python 3.10+
- MySQL Server
- pip

---

## 📦 Installation

### 1️⃣ Clone the Repository

git clone https://github.com/<your-username>/Event-Management
cd Event-Management
2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Create MySQL Database
CREATE DATABASE event_system;

4️⃣ Configure DB Connection

In db.py:

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="event_system"
)

▶️ Running the App
python app.py


Then open:

👉 http://127.0.0.1:5000/



🖼 Screenshots

Below is one screenshot you shared.
You can add more later by uploading them.

🏠 Home Page

(Add more screenshots inside static/images/ and update here.)

🔮 Future Improvements

Login authentication

Admin & staff roles

Calendar event viewer

Export reports to PDF/Excel

Dashboard with charts

Dark mode UI

📄 License

This project is licensed under the MIT License.
