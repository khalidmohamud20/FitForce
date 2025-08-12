# 🏋️ FitForce

Welcome to **FitForce** — your ultimate destination for fitness and well-being! Whether you're here to track your workouts, follow a personalized fitness plan, or gain motivation, FitForce is designed to support your fitness journey every step of the way.

This platform provides easy-to-use features, including workout tracking, meal planning, and progress monitoring to help you reach your goals.

FitForce is a project created as part of my web development journey, focusing on creating an interactive and user-friendly platform for those dedicated to fitness. From design and planning to coding with Django, HTML, and CSS, FitForce reflects my passion for both fitness and development.

---
## Table of Contents

- [🏋️ Core Features](#-core-features)  
- [🛠️ CRUD Functionality (Workouts)](#-crud-functionality-workouts)  
- [👤 User Profile Management](#-user-profile-management)  
- [🌟 User Experience Features](#-user-experience-features)  
- [🛠️ Technology Stack](#-technology-stack)  
- [🎯 Accessibility Features](#-accessibility-features)  
- [⚡ Performance Optimizations](#-performance-optimizations)  
- [🧑‍🤝‍🧑 User Stories](#-user-stories)  
- [Testing](#testing)  
- [💡 Lighthouse Report](#-lighthouse-report)  
- [🚀 Getting Started](#-getting-started)  

## 🧩 Core Features

- **🏋️ Workout Plans**  
  Browse and follow structured workouts (Upper Body, Lower Body, Full Body).

- **📖 Exercise Library**  
  View exercises with descriptions and difficulty levels (Beginner, Intermediate, Advanced).

- **🛠️ CRUD Operations**  
  Create, Read, Update, and Delete workouts via an admin interface or user-facing forms.

- **👤 User Authentication**  
  Register, log in, and manage user accounts securely using Django's built-in auth system.

- **📅 Workout Tracker**  
  Users can track and review their completed workouts over time.

- **🖼️ Visual Workout Cards**  
  Exercises and routines displayed using clean, responsive card components.

- **⚙️ User Profile Management**  
  Update account info and view personalized workout data.

---

## 🛠️ CRUD Functionality (Workouts)

- **Create** 📝  
  Users (or admins) can add new workouts with fields like name, difficulty, and description.

- **Read** 📖  
  Workouts are displayed on the homepage as cards, with details about the exercises.

- **Update** ✏️  
  Existing workout details can be edited and saved.

- **Delete** 🗑️  
  Workouts can be removed from the system when no longer needed.

---

## 👤 User Profile Management

- **Register & Login** 🔐  
  New users can sign up and existing users can log in to access personalized features.

- **Profile Dashboard** 🧾  
  Each user has a dashboard where they can view their workout history and personal info.

- **Update Profile** ⚙️  
  Users can edit their profile details such as name, email, and password.

- **Authentication & Authorization** ✅  
  Access to profile features is protected — only logged-in users can manage their data.

---

## 🌟 User Experience Features

- **💡 Clean & Minimal Design**  
  A distraction-free layout with clear typography and calming visuals.

- **📱 Mobile-Friendly & Responsive**  
  Works smoothly across all screen sizes — desktop, tablet, and mobile.

- **🧭 Intuitive Navigation**  
  Simple menus and layout make it easy to browse workouts, track progress, and manage your profile.

- **⚡ Fast Load Times**  
  Optimized HTML/CSS and minimal assets for speed.

- **📌 Helpful Labels & Feedback**  
  Form validation and clear messaging guide the user experience.

- **🖼️ Visual Workout Cards**  
  Workout routines displayed in card format for quick scanning.

---

## 🛠️ Technology Stack

- **Backend:** Django 5.2.4, Python 3.11  
- **Database:** PostgreSQL (production), SQLite (development)  
- **Frontend:** HTML5, CSS3, JavaScript (AJAX), Responsive Media Queries  
- **Deployment:** Heroku with Gunicorn WSGI server  
- **Static Files:** WhiteNoise for optimized static asset delivery  
- **Database Tools:** pgAdmin  
- **UI/UX:** Mobile-first responsive design

---

## 🎯 Accessibility Features

- **🧩 Semantic HTML**  
  Proper use of HTML5 tags (e.g., `<nav>`, `<main>`, `<section>`) for screen readers.

- **🌈 High Contrast & Readable Fonts**  
  Improves readability for users with visual impairments.

- **🔗 Keyboard Navigable**  
  All interactive elements are accessible via keyboard.

- **📱 Responsive Design**  
  Accessible on all devices — mobile, tablet, and desktop.

---

## ⚡ Performance Optimizations

- **🧹 Clean, Minimal Codebase**  
  Optimized HTML, CSS, and templates.

- **🖼️ Compressed Images**  
  Fast-loading, optimized visual assets.

- **📦 Static File Management**  
  Efficient serving of CSS, JS, and images using Django static files.

- **🚫 No Unused Libraries**  
  Only necessary dependencies included.

- **⏱️ Fast Page Loads**  
  Minimal external requests and efficient templates.

---

## 🧑‍🤝‍🧑 User Stories

- **As a new user**, I want to easily register and log in, so I can start tracking my workouts.  
- **As a returning user**, I want to view my workout history, so I can stay consistent and track progress.  
- **As someone new to fitness**, I want to see beginner-friendly exercises, so I can feel confident and not overwhelmed.  
- **As a regular gym-goer**, I want to access structured workout plans, so I can follow a routine without wasting time.  
- **As a user with limited time**, I want a clean, fast-loading site, so I can quickly find and start my workouts.  
- **As an admin/developer**, I want to create, update, and delete workouts, so I can keep the content fresh and relevant.


## Testing

To make sure everything works well, I tested the site in several ways:

- ✅ Used [W3C HTML Validator](https://validator.w3.org/) to check HTML validity  
- ✅ Used [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS  
- ✅ Ran Lighthouse audits to assess performance, accessibility, and SEO  
- ✅ Manually tested on desktop, mobile, and tablet using multiple browsers  
### Lighthouse Report

Below is the Lighthouse report showing strong performance across all key categories:

## 💡Lighthouse Report

![Lighthouse report](workouts/static/images/lighthouse%20pic%20fit%20force%20.png)

- 🟢 **Performance:** 95+ — Fast loading times with optimized static files and responsive images  
- ♿ **Accessibility:** 70+ — WCAG 2.1 compliant with comprehensive screen reader support  
- 📱 **Best Practices:** 95+ — Modern web standards with secure HTTPS deployment  
- 🔍 **SEO:** 90+ — Semantic HTML structure with proper meta tags and descriptions  


## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL (for local development with pgAdmin)
- Git

### Local Installation

1. **Clone the repository:**
```bash
git clone https://github.com/DavidShergold/capstone-shopping-quest.git
cd capstone-shopping-quest
```

2. **Create virtual environment:**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up local database (optional - uses SQLite by default):**
```bash
# For PostgreSQL setup, copy and modify:
cp local_settings_example.py shoppingquest/local_settings.py
# Edit local_settings.py with your PostgreSQL credentials
```

5. **Run migrations:**
```bash
python manage.py migrate
```

6. **Create superuser (optional):**
```bash
python manage.py createsuperuser
```

7. **Run development server:**
```bash
python manage.py runserver
```
