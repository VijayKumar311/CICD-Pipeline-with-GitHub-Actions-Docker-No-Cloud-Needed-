# my-app

Sample Flask app used to demonstrate CI/CD with GitHub Actions and Docker.

## Structure

- app/: Flask application source code
- tests/: pytest test files
- Dockerfile, docker-compose.yml
- .github/workflows/ci-cd.yml : GitHub Actions workflow

## Run locally

```bash
docker compose up --build
```

Then visit: http://localhost:5000
