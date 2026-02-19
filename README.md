# role_auth_backend (Django + DRF + JWT + Roles)

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Create demo users

Open Django shell:

```bash
python manage.py shell
```

Then run:

```python
from accounts.models import User
User.objects.create_user(email="admin@demo.com", password="Admin@1234", name="Admin", role="admin")
User.objects.create_user(email="user@demo.com", password="User@1234", name="User", role="user")
```

## API

- POST `/api/auth/login/` { email, password }
- POST `/api/auth/refresh/` { refresh }
- GET `/api/auth/me/` (Bearer access token)
- GET `/api/admin/stats/` (admin role)
- GET `/api/user/summary/` (user role)
