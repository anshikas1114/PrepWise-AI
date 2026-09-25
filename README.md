# PrepWise AI

> An AI-powered interview preparation platform designed to help students and job seekers prepare for technical, HR, and behavioral interviews.

## 📌 About the Project

PrepWise AI is a web-based interview preparation platform being developed as a major project.

The platform is designed to provide users with a structured environment where they can create an account, manage their profile, prepare for interviews, answer interview questions, receive performance feedback, and identify areas that need improvement.

The project focuses on combining a user-friendly web application with AI-assisted interview preparation and personalized recommendations.

### Current Development Status

The project is currently in the **M1 - Backend Foundation and User Profile Management** phase.

The current implementation includes:

- Django backend setup
- PostgreSQL database integration
- User registration
- Automatic login after registration
- User profile creation and management
- Interview and question data models
- Django administration panel
- Basic application routing

Additional interview, evaluation, recommendation, and AI features will be implemented in subsequent development phases.

---

## 🎯 Objectives

The main objectives of PrepWise AI are:

- Provide users with a centralized interview preparation platform.
- Allow users to create and manage their personal profiles.
- Store user skills, education, experience level, and target role.
- Provide different types of interview preparation.
- Organize interview questions according to category, skill, and difficulty.
- Record user interview responses and performance.
- Provide meaningful feedback on interview performance.
- Identify areas where users need additional preparation.
- Generate personalized recommendations based on user performance.
- Provide a simple and accessible interface for students and job seekers.

---

## ✨ Planned Features

### 👤 User Authentication

Users will be able to:

- Register for an account
- Log in securely
- Log out
- Access their personal account
- Manage their profile

### 📝 Profile Management

Users will be able to maintain information such as:

- Full name
- Education
- Skills
- Experience level
- Target job role
- Personal introduction/bio

### 🎤 Interview Preparation

The platform is planned to support different interview categories:

- Technical interviews
- HR interviews
- Behavioral interviews
- Mixed interviews

Users will also be able to select an appropriate difficulty level.

### ❓ Question Management

Interview questions will be organized using information such as:

- Category
- Skill
- Difficulty
- Expected answer

This structure will allow questions to be used efficiently during interview sessions.

### 📊 Performance Evaluation

The planned evaluation system will analyze user responses and provide:

- Scores
- Feedback
- Performance information
- Areas requiring improvement

### 🤖 AI-Assisted Preparation

Future development will introduce AI-based functionality to help with:

- Interview question generation
- Answer evaluation
- Similarity-based analysis
- Personalized feedback
- Skill-gap identification
- Preparation recommendations

### 💡 Personalized Recommendations

The platform is planned to recommend topics and preparation areas based on the user's interview performance.

---

## 🏗️ Project Architecture

The current backend is structured using Django applications.

```text
PrepWise-AI/
│
├── .gitignore
├── README.md
│
└── backend/
    │
    ├── manage.py
    ├── requirements.txt
    │
    ├── config/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── accounts/
    │   ├── views.py
    │   ├── urls.py
    │   └── templates/
    │
    ├── profiles/
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── templates/
    │
    ├── questions/
    │   ├── models.py
    │   └── admin.py
    │
    ├── interviews/
    │   ├── models.py
    │   └── admin.py
    │
    ├── evaluation/
    │
    └── recommendations/
        ├── models.py
        └── admin.py