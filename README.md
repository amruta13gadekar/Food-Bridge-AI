# 🍲 Food Bridge AI

> **A Flask-based web platform connecting food donors with NGOs to reduce food waste and help people in need.**

---

## 📌 Project Overview

**Food Bridge AI** is a web-based food donation platform designed to reduce food waste by connecting food donors with NGOs and people in need.

The platform allows hotels, restaurants, event organizers, and other donors to share surplus food with NGOs. NGOs can view available food donations and accept suitable donations for collection.

---

## 🎯 Objectives

* Reduce food wastage
* Connect food donors with NGOs
* Make food donation simple and accessible
* Help distribute surplus food to people in need
* Use technology to make the donation process more efficient

---

## ✨ Features

* 👤 Donor and NGO registration
* 🔐 User login system
* 🍱 Food donation form
* 📍 Donation location and contact details
* 📋 View available food donations
* ✅ NGOs can accept donations
* 🤖 AI-based food prediction
* 🗄️ MySQL database integration
* 🌐 User-friendly web interface

---

## 🛠️ Technologies Used

| Category         | Technologies                        |
| ---------------- | ----------------------------------- |
| Frontend         | HTML, CSS, Bootstrap, JavaScript    |
| Backend          | Python, Flask                       |
| Database         | MySQL                               |
| Machine Learning | Pandas, NumPy, Scikit-learn, Joblib |

---

## 📂 Project Structure

```text
Food-Bridge-AI/
│
├── app.py
├── model.pkl
├── encoder.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── donate.html
│   └── donations.html
│
└── static/
    ├── css/
    ├── images/
    └── js/
```

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/amruta13gadekar/Food-Bridge-AI.git
```

### 2. Open the Project

```bash
cd Food-Bridge-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Create a MySQL database named:

```text
foodbridge
```

Then configure your MySQL username, password, and database details in `app.py`.

### 7. Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 🔄 How It Works

### 1. Register

Donors and NGOs create an account on the platform.

### 2. Login

Users log in according to their role.

### 3. Donate Food

Donors enter information about their surplus food.

### 4. View Donations

NGOs can view available food donations.

### 5. Accept Donation

An NGO can accept a suitable donation.

### 6. Food Distribution

The donated food can be collected and distributed to people in need.

---

## 🤖 AI Component

The project includes a machine learning component for food-related prediction/classification.

The trained machine learning files are:

```text
model.pkl
encoder.pkl
```

The model is integrated with the Flask application.

---

## 🌱 Benefits

* ♻️ Helps reduce food waste
* 🤝 Supports NGOs and communities
* 🍱 Encourages responsible food sharing
* 🌍 Helps provide food to people in need
* 💻 Provides a simple digital platform for food donation
* 🔗 Connects food donors and NGOs efficiently

---

## 🚀 Future Enhancements

* 📍 Google Maps integration for donation locations
* 🔔 Real-time notifications
* 📧 Email/SMS notifications
* 🏢 NGO verification
* 📊 Donation history and tracking
* 📱 Mobile application
* 🤖 Improved AI prediction
* 🔄 Real-time donation status



