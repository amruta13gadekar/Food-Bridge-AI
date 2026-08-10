# Food-Bridge-AI
A Flask-based web platform connecting food donors with NGOs to reduce food waste and help people in need.

🍲 Food Bridge AI
📌 Project Overview

Food Bridge AI is a web-based food donation platform designed to reduce food waste and help connect food donors with NGOs and people in need.

The platform allows hotels, restaurants, event organizers, and other donors to share surplus food with NGOs. NGOs can view available food donations and accept suitable donations for collection.

🎯 Objectives
Reduce food wastage
Connect food donors with NGOs
Make food donation simple and accessible
Help distribute surplus food to people in need
Use technology to make the donation process more efficient
✨ Features
👤 Donor and NGO registration
🔐 Secure login system
🍱 Food donation form
📍 Donation location and contact details
📋 View available food donations
✅ NGOs can accept donations
🤖 AI-based food prediction
🗄️ MySQL database integration
🌐 User-friendly web interface
🛠️ Technologies Used
Frontend
HTML
CSS
Bootstrap
JavaScript
Backend
Python
Flask
Database
MySQL
AI / Machine Learning
Python
Pandas
NumPy
Scikit-learn
Joblib
📂 Project Structure
Food-Bridge-AI/
│
├── app.py
├── model.pkl
├── encoder.pkl
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── donate.html
│   └── donations.html
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
└── README.md
⚙️ How to Run the Project
1. Clone the repository
git clone https://github.com/amruta13gadekar/Food-Bridge-AI.git
2. Open the project
cd Food-Bridge-AI
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows:

venv\Scripts\activate
5. Install required packages
pip install -r requirements.txt
6. Configure MySQL

Create a MySQL database named:

foodbridge

Then configure the MySQL username, password, and database details in app.py.

7. Run the Flask application
python app.py

Open the application in your browser:

http://127.0.0.1:5000/
🔄 How It Works
Register – Donors and NGOs create an account.
Login – Users log in according to their role.
Donate Food – Donors enter information about surplus food.
View Donations – NGOs can see available food donations.
Accept Donation – An NGO can accept a suitable donation.
Food Distribution – The donated food can then be collected and distributed to people in need.
🤖 AI Component

The project includes a machine learning component that helps predict/classify food-related information using a trained model.

The trained model and encoder are stored as:

model.pkl
encoder.pkl
🌱 Benefits
Helps reduce food waste
Supports NGOs and communities
Encourages responsible food sharing
Provides a simple digital platform for food donation
Connects donors and organizations efficiently

🚀 Future Enhancements
Google Maps integration for donation locations
Real-time notifications
Email/SMS notifications
NGO verification
Donation history and tracking
Mobile application
Improved AI prediction
Real-time donation status