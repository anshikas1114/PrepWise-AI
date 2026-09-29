# PrepWise AI

### AI-Powered Interview Preparation & Career Readiness Platform

PrepWise AI is a Django-based interview preparation platform designed to help students and job seekers practice interviews in a structured and measurable environment.

The platform allows users to create an account, manage their professional profile, configure interview sessions, answer interview questions, and track their interview performance.

The project is being developed in phases, with future modules focused on AI-based answer evaluation, personalized feedback, performance analytics, recommendations, and timed technical coding interviews.

---

## 📌 Project Overview

Preparing for interviews using scattered resources can make it difficult to evaluate actual interview readiness. Students may know the concepts but still struggle with answering questions under pressure, identifying weak areas, and receiving meaningful feedback.

PrepWise AI aims to provide a single platform where users can:

- Create and manage their account
- Maintain their interview preparation profile
- Select interview type and difficulty
- Practice role-specific interview questions
- Submit and store interview responses
- Complete structured interview sessions
- View interview results
- Receive AI-based evaluation and feedback *(upcoming)*
- Track performance over multiple interviews *(upcoming)*
- Receive personalized preparation recommendations *(upcoming)*
- Practice timed technical coding questions *(upcoming)*

---

## 🎯 Objectives

The main objectives of PrepWise AI are:

- Provide a structured interview practice environment.
- Support different interview categories such as Technical, HR, Behavioral, and Mixed interviews.
- Allow users to specify their target job role and difficulty level.
- Maintain user profiles containing education, skills, experience level, and target role.
- Store interview questions and user responses in a structured database.
- Evaluate answers using AI-based techniques.
- Provide meaningful feedback on interview performance.
- Identify areas where users need improvement.
- Generate personalized preparation recommendations.
- Provide a timed coding environment for technical interviews.

---

## 🚀 Current Features

### Authentication

- User registration
- User login
- User logout
- Protected pages using Django authentication
- Automatic redirection after authentication
- Session-based authentication

### User Dashboard

The dashboard provides access to:

- User profile
- Interview preparation
- Performance section
- Recommendations section
- Logout

### Profile Management

Users can maintain:

- Full Name
- Education
- Skills
- Experience Level
- Target Role
- Bio

### Interview Configuration

Users can create an interview session by selecting:

- Interview Type
  - Technical
  - HR
  - Behavioral
  - Mixed
- Target Role
- Difficulty
  - Easy
  - Medium
  - Hard

### Interview Session

The current interview workflow supports:

- Question retrieval based on category and difficulty
- Question-by-question navigation
- Answer submission
- Response storage
- Question progress tracking
- Interview completion

### Interview Completion

After completing an interview, the system currently displays:

- Target Role
- Interview Type
- Difficulty
- Interview Score
- Completion status

The completion page also contains a dedicated area for future AI-generated feedback.

---

## 🤖 Upcoming AI Features

The next major development stage will introduce the intelligent components of PrepWise AI.

### AI Answer Evaluation

The system will evaluate submitted answers based on factors such as:

- Relevance
- Semantic similarity
- Answer quality
- Expected answer alignment

Each response will eventually receive:

- Score
- Feedback
- Similarity score
- Improvement suggestions

### Performance Analytics

The platform will analyze previous interviews and provide:

- Overall performance
- Question-wise performance
- Strength areas
- Weak areas
- Interview history
- Progress over time

### Personalized Recommendations

Based on interview performance, the system will recommend:

- Topics to revise
- Skills to improve
- Question categories to practice
- Suggested interview difficulty
- Personalized preparation activities

### Timed Technical Coding

A dedicated technical interview mode is planned with:

- Programming questions
- Countdown timer
- Code editor
- Test cases
- Code submission
- Result evaluation

---

## 🛠️ Technology Stack

### Backend

- Python
- Django 5.2.17

### Database

- PostgreSQL

### Frontend

- HTML5
- CSS3
- JavaScript

### Development Tools

- Visual Studio Code
- Git
- GitHub

### Planned AI / Evaluation Components

- Semantic similarity
- AI-based answer evaluation
- Automated feedback generation

---

## 🏗️ Project Structure

```text
PrepWise-AI/
│
├── backend/
│   │
│   ├── accounts/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── profiles/
│   │   ├── templates/
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── interviews/
│   │   ├── templates/
│   │   ├── migrations/
│   │   ├── models.py
│   │   └── views.py
│   │
│   ├── questions/
│   │   ├── migrations/
│   │   ├── models.py
│   │   └── views.py
│   │
│   ├── evaluation/
│   │   ├── models.py
│   │   └── views.py
│   │
│   ├── recommendations/
│   │   ├── models.py
│   │   └── views.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── manage.py
│   └── requirements.txt
│
├── docs/
│   ├── PrepWise_AI_Synopsis.pdf
│   ├── PrepWise_AI_SRS.pdf
│   └── PrepWise_AI_Project_Documentation.pdf
│
├── .gitignore
└── README.md