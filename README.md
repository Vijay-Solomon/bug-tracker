🐞 Bug Tracker System (Mini Jira Clone)

A full-stack Bug Tracking System built using Python, Flask, SQLAlchemy, WTForms, and deployed on Render.
This project implements essential features similar to Jira/Linear and is perfect for showcasing backend development skills.

🚀 Live Demo

🔗 https://bug-tracker-25wk.onrender.com

📌 Features
👤 User System

Register/Login

Admin, Developer, Tester roles

Role-based access control

🐛 Ticket Management

Create new tickets

Assign to users

Set priority (Low/Medium/High)

Update ticket status

Delete tickets

Detailed ticket view

Export tickets to CSV

🔍 Filtering & Search

Filter by status

Filter by priority

Search by title

🗂 Tech Used

Python 3.11

Flask

SQLAlchemy

WTForms

SQLite

Gunicorn

Render (deployment)

📁 Project Structure
bug-tracker/
│── app/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│
│── run.py
│── init_db.py
│── sample_data.py
│── requirements.txt
│── Procfile
│── config.py
│── README.md

🛠 Installation (Local Setup)
1️⃣ Clone the repository
git clone https://github.com/Vijay-Solomon/bug-tracker.git
cd bug-tracker

2️⃣ Create a virtual environment
python3.11 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Initialize the database
python init_db.py
python sample_data.py

5️⃣ Start the app
python run.py


Open browser:

👉 http://127.0.0.1:5000

🚀 Deployment (Render)

This app is deployed using Render with:

requirements.txt for dependencies

Procfile for Gunicorn

Start command:

web: gunicorn run:app

🎯 Future Improvements

Ticket comments

Email notifications

Activity log

Analytics dashboard

Dark mode

👨‍💻 Author

Vijay Solomon
Python Developer | MCA Graduate
Feel free to connect
