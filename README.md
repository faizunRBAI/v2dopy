# v2dopy

A Python/Django web application deployed on a DigitalOcean Droplet (nyc1).

## Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11 |
| Framework | Django 4.2 |
| WSGI Server | Gunicorn |
| Reverse Proxy | Nginx |
| Database | PostgreSQL (local) |
| IaC | Terraform (DigitalOcean provider) |
| Config Mgmt | Ansible |
| CI/CD | GitHub Actions (UDAP) |

## Local Development

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set environment variables
cp .env.example .env
# Edit .env with your local values

# 4. Run migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

Open http://localhost:8000 in your browser.

## Running Tests

```bash
pip install -r requirements.txt
pytest
```

## Project Structure

```
v2dopy/          Django project settings
api/             Main application (views, models, urls)
infra/           Terraform IaC (DigitalOcean Droplet, Firewall)
ansible/         Ansible playbook for server configuration
```

## Deployment

Deployments are triggered automatically via GitHub Actions on the `main` branch
through the UDAP platform. The pipeline runs:

1. **lint** — flake8 code quality check
2. **test** — Django test suite
3. **provision** — Terraform creates the Droplet + Firewall
4. **configure** — Ansible installs dependencies, configures Nginx/Gunicorn, runs migrations
5. **verify** — curl health-check against the live server

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Set to `True` for local dev only |
| `DATABASE_URL` | PostgreSQL connection URL |
| `ALLOWED_HOSTS` | Comma-separated allowed hostnames |
