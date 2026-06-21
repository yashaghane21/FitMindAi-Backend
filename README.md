# 🧠 FitMind AI Backend

AI-Powered Body Transformation Coach Backend built with FastAPI, MongoDB, JWT Authentication, and AI-ready architecture.

## 🚀 Overview

FitMind AI is an intelligent fitness coaching platform designed to help users achieve:

* Weight Loss
* Weight Gain
* Muscle Gain
* Body Recomposition

Unlike traditional calorie trackers, FitMind AI aims to act as a personal fitness coach by analyzing progress, generating recommendations, calculating nutrition targets, and providing AI-powered guidance.

---

## 🏗️ Tech Stack

### Backend

* FastAPI
* Python
* JWT Authentication
* Motor (Async MongoDB Driver)

### Database

* MongoDB Atlas
* Redis (Planned)

### AI & Machine Learning (Planned)

* LangChain
* ChromaDB
* HuggingFace Embeddings
* Qwen
* Gemma
* Scikit-Learn
* XGBoost

### Mobile App

* React Native
* TypeScript
* Redux Toolkit

---

## 📁 Project Structure

```text
FitMind_AI_Backend/

├── core/
│   ├── security.py
│   └── dependencies.py
│
├── database/
│   └── db.py
│
├── routes/
│   ├── auth.py
│   └── profile.py
│
├── schemas/
│   ├── user_schema.py
│   └── profile_schema.py
│
├── services/
│   └── auth_service.py
│
├── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ✨ Features Implemented

### Authentication Module

* User Registration
* User Login
* Password Hashing using bcrypt
* JWT Access Tokens
* Protected Routes
* Current User Extraction

### Profile Module

* Update User Profile
* Get User Profile
* Goal Management
* Activity Level Tracking

---

## 🔐 Authentication Flow

```text
User Login
     ↓
Generate JWT Token
     ↓
Protected API Request
     ↓
JWT Verification
     ↓
Access Granted
```

---

## 🧾 User Profile Fields

```json
{
  "age": 21,
  "gender": "male",
  "height": 173,
  "weight": 67,
  "goal": "muscle_gain",
  "activity_level": "very_active"
}
```

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint       | Description            |
| ------ | -------------- | ---------------------- |
| POST   | /auth/register | Register User          |
| POST   | /auth/login    | Login User             |
| GET    | /auth/me       | Current Logged-In User |

### Profile

| Method | Endpoint | Description         |
| ------ | -------- | ------------------- |
| GET    | /profile | Get User Profile    |
| PUT    | /profile | Update User Profile |

---

## 🛣️ Upcoming Features

### Nutrition Engine

* BMR Calculator
* TDEE Calculator
* Macro Calculator
* Goal Calories Calculator

### Weight Tracking

* Daily Weight Logs
* Progress Analytics
* Transformation Tracking

### Food Logging

* Calorie Tracking
* Protein Tracking
* Macro Tracking

### AI Coach

* Nutrition Q&A
* Progress Analysis
* Smart Recommendations
* Personalized Coaching

### RAG Knowledge Base

* Nutrition Research
* Scientific Studies
* Fitness Articles

### Offline AI

* ONNX
* Gemma
* Qwen
* llama.cpp

---

## ⚙️ Environment Variables

Create a `.env` file:

```env
MONGO_URI=your_mongodb_connection_string

MONGO_DB_NAME=fitmind

SECRET_KEY=your_secret_key
```

---

## 🚀 Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start server:

```bash
uvicorn main:app --reload
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 🎯 Project Goals

This project demonstrates:

* Backend Engineering
* FastAPI Development
* Authentication & Security
* Database Design
* API Development
* System Design
* AI Engineering Foundations
* Production-Grade Architecture

---

## 👨‍💻 Author

Yash Aghane

Computer Engineering Student | Full Stack Developer | AI Enthusiast

Building FitMind AI to combine Fitness, Artificial Intelligence, and Software Engineering into a real-world product.
