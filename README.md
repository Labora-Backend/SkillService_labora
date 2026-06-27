# Skill Service

Skill Service manages the platform skill catalog and freelancer-to-skill assignments. It exposes public skill reads, role-protected skill assignment APIs, and internal skill administration endpoints used by Admin Service and Freelancer Profile Service.

## Responsibilities

- Store skill catalog entries.
- Allow admins to create skills through the public admin-protected API.
- Allow freelancers to add or remove skills from their own profile.
- Return skills for a given freelancer.
- Provide internal CRUD endpoints for Admin Service.

## Features

- Skill listing without authentication.
- Admin-only skill creation.
- Freelancer-only skill assignment and removal.
- Duplicate freelancer skill assignment prevented with a model-level uniqueness constraint.
- Internal user-skill lookup for profile enrichment.

## API Endpoints

Base path: `/api/`

| Method | Path | Auth | Description |
| --- | --- | --- | --- |
| `GET` | `skills/` | Public | List all skills. |
| `POST` | `skills/create/` | Admin JWT | Create a skill. |
| `POST` | `freelancer/skills/add/` | Freelancer JWT | Add a skill to the authenticated freelancer. |
| `DELETE` | `freelancer/skills/remove/<id>/` | Freelancer JWT | Remove one of the authenticated freelancer's skill records. |
| `GET` | `freelancer/<user_id>/skills/` | Public | List skills for a freelancer user id. |

## Internal Service Endpoints

Internal endpoints use `X-Service-Key: <SERVICE_API_KEY>`.

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `internal/users/<user_id>/skills/` | Return skills for one user. |
| `GET` | `internal/skills/` | List all skills ordered by name. |
| `POST` | `internal/skills/` | Create a skill. |
| `GET` | `internal/skills/<skill_id>/` | Return one skill. |
| `PUT` | `internal/skills/<skill_id>/` | Replace one skill. |
| `DELETE` | `internal/skills/<skill_id>/` | Delete one skill. |

## Authentication

Role-protected APIs use the shared RS256 JWT public key. Internal APIs bypass JWT and require `X-Service-Key`.

## Environment Variables

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Django secret key. |
| `DEBUG` | Enables debug mode when set to `1`, `true`, or `yes`. |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts. Defaults to `*`. |
| `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` | MySQL database configuration. |
| `JWT_PUBLIC_KEY_PATH` | Public key used to verify Auth Service JWTs. |
| `SERVICE_API_KEY` | Shared key for internal service endpoints. |
| `*_SERVICE_URL` | Optional service URL settings loaded by settings. |

## Setup

```bash
cd SkillService_labora
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8006
```

## Service Architecture

- Django project: `skillservice`
- App: `skills`
- Authentication: `skills.authentication.CustomJWTAuthentication`
- Role decorators: top-level `authentication.py`
- Internal permission: `skills.permissions.internal_service.IsInternalService`

## Database Models

- `Skill`: skill name.
- `UserSkill`: `user_id` plus foreign key to `Skill`; unique per user/skill pair.

## Notification/Event Flow

This service does not emit notifications or WebSocket events.
