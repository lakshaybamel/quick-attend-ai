# 🚀 Quick Attend

<p align="center">
  <img src="https://i.ibb.co/Y7RhZHfF/Quick-Attend-Logo.png" width="150" alt="QuickAttend Logo"/>
</p>

<h3 align="center">
AI-powered Smart Attendance System using Face Recognition, Voice Recognition, Streamlit, and Supabase
</h3>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit"/>
<img src="https://img.shields.io/badge/Supabase-Backend-green?style=for-the-badge&logo=supabase"/>
<img src="https://img.shields.io/badge/AI-Face%20Recognition-purple?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Voice-Recognition-orange?style=for-the-badge"/>

</p>

<p align="center">
Smart • Fast • AI-powered Attendance Automation
</p>

---

## 🌐 Live Demo

🔗 **App:** https://quickattend.streamlit.app/

---

## 📖 Overview

Quick Attend is a smart attendance management platform designed to automate classroom attendance using Artificial Intelligence.

Traditional attendance systems require manual roll calls and consume valuable class time. Quick Attend replaces this process using **Face Recognition** and **Voice Recognition**, allowing teachers to mark attendance automatically.

The platform includes separate Teacher and Student portals, subject management, QR-based enrollment, AI-powered attendance workflows, and attendance history tracking.

---

## ✨ Features

### 👨‍🏫 Teacher Portal

* Create and manage subjects
* Generate subject join links
* Generate QR codes for enrollment
* View total enrolled students
* Track attendance history
* Face Recognition attendance
* Voice Recognition attendance

### 🎓 Student Portal

* Student profile registration
* Face profile setup
* Voice profile setup
* Join subjects using QR or code
* View enrolled subjects
* View attendance records

### 🤖 AI Features

* Automatic face detection
* Face embeddings generation
* Speaker recognition
* Attendance prediction using AI
* Automatic attendance logging

---

## 🧠 AI Workflow

### Face Recognition Pipeline

```text
Class Image
   ↓
Face Detection (Dlib)
   ↓
Face Embeddings
   ↓
SVM Classification
   ↓
Student Matching
   ↓
Attendance Logging
```

### Voice Recognition Pipeline

```text
Classroom Audio
   ↓
Audio Processing
   ↓
Voice Embeddings
   ↓
Similarity Matching
   ↓
Student Identification
   ↓
Attendance Logging
```

---

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Supabase

### Database

* PostgreSQL (Supabase)

### Machine Learning / AI

* Dlib
* Scikit-learn
* Resemblyzer
* Face Recognition Models

### Libraries

* NumPy
* Pandas
* Librosa
* Segno
* Pillow
* Bcrypt

---

## 📂 Project Structure

```bash
quick-attend-ai/
│
├── .streamlit/
│   ├── config.toml
│
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   └── ui/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup

Clone repository:

```bash
git clone https://github.com/lakshaybamel/quick-attend-ai.git

cd quick-attend-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create:

```bash
.streamlit/secrets.toml
```

Add:

```toml
SUPABASE_URL="your_url"
SUPABASE_KEY="your_key"
```

Run locally:

```bash
streamlit run app.py
```

---

## 🚀 Deployment

Quick Attend is deployed using:

* Streamlit Community Cloud
* Supabase Backend
* Python 3.14

---

## 🔮 Future Improvements

* Attendance analytics dashboard
* Export attendance reports
* Attendance percentage visualization
* Better multi-speaker recognition
* Admin portal
* Enhanced classroom insights

---

## 👨‍💻 Developer

**Lakshay Bamel**

GitHub: https://github.com/lakshaybamel

---

## ⭐ Support

If you found this project useful, consider giving it a star.
