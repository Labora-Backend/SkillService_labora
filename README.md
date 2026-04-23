# Skill Service

This is a Django-based service for managing skills in my microservice backend project.

This service handles skill-related operations like creating skills and assigning them to users.

---

## What this service does

* Create and manage skills
* Assign skills to users (freelancers)
* Remove skills from users
* Provide APIs for skill-related operations

---

## Tech Used

* Python
* Django
* Django REST Framework
* Docker

---

## Project Structure

```text id="rwr1i9"
SkillService/
│
├── skills/               # App logic (models, views, serializers)
├── skillservice/         # Main Django project
├── manage.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
└── README.md
```

---

## API Endpoints (basic)

* GET `/skills/` → list skills
* POST `/skills/create/` → create skill
* POST `/freelancer/skills/add/` → add skill to user
* DELETE `/freelancer/skills/remove/<id>/` → remove skill
* GET `/freelancer/<user_id>/skills/` → get user skills

---

## How to Run

### 1. Clone

```bash id="l6t5v7"
git clone https://github.com/YOUR-USERNAME/SkillService.git
cd SkillService
```

### 2. Setup environment

```bash id="8b2jbo"
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash id="9plr8y"
pip install -r requirements.txt
```

### 4. Run migrations

```bash id="h5nt6p"
python manage.py migrate
```

### 5. Run server

```bash id="7yyk1d"
python manage.py runserver
```

---

## Run with Docker

```bash id="s4k9hg"
docker build -t skill-service .
docker run -p 8000:8000 skill-service
```

---

## Notes

* `.env`, `.pem`, and sensitive files are ignored
* This service is part of a larger backend system

---
