# omilabs_kumo_django

A production-ready Django application deployed using Docker, Nginx, PostgreSQL, GitHub Actions, and a Hetzner VPS.
The project includes a full CI/CD pipeline with Trivy image scanning, automated deployments, secure configurations, and structured debugging tools.



# 📌 Overview

omilabs_kumo_django is a production-ready Django application deployed to a Hetzner VPS using a hardened DevOps stack featuring:

* Docker & Docker Compose
* Nginx reverse proxy & SSL
* Gunicorn application server
* PostgreSQL database
* GitHub Actions CI/CD
* GHCR (GitHub Container Registry)
* Trivy vulnerability scanning
* Automated deployments with SSH + scripts

This represents a real-world deployment architecture similar to what modern DevOps teams use in cloud-native production environments.


# ⭐ Key Highlights
**🔹 Production-ready Architecture**

  * Reverse proxy (Nginx) with HTTPS
  * Gunicorn serving Django
  * PostgreSQL with persistent volumes
  * Static & media storage separated from the app
  * Secure secret management

**🔹 End-to-End CI/CD**

  * Build → Scan → Push → Deploy
  * Fully automated GitHub Actions workflow
  * SSH deployment to Hetzner
  * Auto rollback capability through re-runs
  * Detections for missing secrets

🔹 Security (DevSecOps)

  * Trivy scans Docker images and dependencies
  * GHCR for secure private image hosting
  * Strict SSH key handling
  * SSL/TLS with Let’s Encrypt

**🔹 Observability & Debugging**

  * Healthchecks for container readiness
  * Nginx & application logs
  * Docker network inspection
  * Remote debugging via SSH


# 🧱 Architecture

           ┌──────────────────────────┐
           │      GitHub Actions      │
           │  Build → Scan → Push     │
           └──────────────┬───────────┘
                          │
                    GHCR Image Push
                          │
           ┌──────────────▼───────────┐
           │       Hetzner VPS        │
           │  Ubuntu + Docker Engine  │
           └──────────────┬───────────┘
                          │
                docker compose up -d
                          │
┌─────────────────────────────────────────────┐
│               Docker Services               │
│                                             │
│   ┌─────────┐      ┌──────────────┐         │
│   │  NGINX  │─────▶│ GUNICORN     │──────┐ │
│   └─────────┘      │ Django App   │      │ │
│                    └──────────────┘       │ │
│                      ▲       │            │ │
│                      │       │ static/media │
│               ┌──────┴───┐  ┌────▼───────┐│ │
│               │ Certbot  │  │ PostgreSQL ││ │
│               └──────────┘  └────────────┘│ │
└─────────────────────────────────────────────┘


# 📁 Project Structure

milabs_kumo_django/
│
├── Dockerfile # App image build (with curl + security best-practices)
├── docker-compose.yml # Production orchestration stack
│
├── nginx/
│ └── default.conf # Nginx reverse proxy + SSL config
│
├── scripts/
│ └── deploy.sh # Executes deployment on the VPS
│
├── .github/workflows/
│ ├── build.yml # Builds & pushes Docker image → GHCR
│ ├── deploy.yml # Deploy pipeline (workflow_run)
│ └── security_scan.yml # Trivy vulnerability scan
│
├── requirements.txt
├── requirements-prod.txt
└── Kumo/… Django project files



---

# 🏗️ CI/CD Pipeline Overview

The pipeline has **three main workflows**:

---

## 1️⃣ CI: Build & Push Docker Image (GHCR)

- Builds the image using Dockerfile
- Tags image as:  
  `ghcr.io/omilabs/kumo_django:stage`
- Authenticates to GHCR
- Pushes image
- Runs Trivy scan (optional fail on high CVEs)

---

## 2️⃣ CI: Security Scan (Trivy)

Trivy scans:

- Docker image
- File system
- Dependencies (`requirements*.txt`)

Example Trivy job:

```yaml
- name: Run Trivy Image Scan
  uses: aquasecurity/trivy-action@v0.11.2
  with:
    image-ref: ghcr.io/omilabs/kumo_django:stage
    format: table
    exit-code: 0
    severity: HIGH,CRITICAL
```

## 3️⃣ CD: Deploy to Hetzner VPS

Triggered when build workflow succeeds.

Deployment steps:

   1. Connect to Hetzner via SSH
   2. Validate secrets
   3. Pull latest repo version
   4. Pull GHCR image
   5. Restart stack
   6. Run post-deploy checks
   7. Optional: Slack/Email notifications

Workflow ensures idempotent, safe, repeatable deployments.

### 🐳 Dockerfile Overview

Your Dockerfile uses:

  * python:3.12-slim
  * System update + curl install (required for healthchecks)
  * Separate requirements for prod vs base
  * Copies Django application
  * Gunicorn entrypoint

Key security features:

  * --no-cache-dir for pip
  * Only installing necessary deps
  * Non-root user (optional upgrade)
  * Slim base image reduces attack surface

### 🛠️ Deploy Script (scripts/deploy.sh)

This script runs inside the VPS during deployment.

What it does:

   1. Checks for Docker & Git availability
   2. Ensures /opt/omilabs_kumo_django exists
   3. Clones repo if missing
   4. Performs Git hard reset to latest commit
   5. Logs into GHCR (if required)
   6. Pulls new image
   7. Restarts stack
   8. Cleans unused Docker images
   9. Reports status back to GitHub Action

**Why a script?**

  * Deployment logic is versioned with code
  * Changes are auditable
  * Allows retries & remote logs
  * Simplifies GitHub Actions workflow (single SSH call)

## 🌍 Domain → Server Communication

When a request comes to:

```
https://stage.omilabs.de
```
Flow:


```
DNS (A record) → Hetzner public IP
→ Nginx (Docker)
→ proxy_pass http://web:8000
→ Gunicorn
→ Django

```

DNS Setup:
```
A record
stage.omilabs.de → <Hetzner VPS IP>
```

Ports:

```
8000 (not exposed to the internet)

```

## 🔐 SSL Certificates

Obtained using this command on the VPS:

```
sudo certbot certonly --webroot -w /var/www/certbot -d stage.omilabs.de

```

Nginx uses:

```
/etc/letsencrypt/live/stage.omilabs.de/fullchain.pem
/etc/letsencrypt/live/stage.omilabs.de/privkey.pem

```

Mounted into the Nginx container.


## 🔍 Debugging Tools & Processes

This is especially important for production operations.

1️⃣ **Check container logs**

```
docker compose logs web --tail 100
docker compose logs nginx --tail 100

```

2️⃣ **Check health status**

```
docker inspect kumo_web | grep -A5 Health

```


3️⃣ **Enter Django container**

```
docker exec -it kumo_web sh

```

**Check app is running:**

```
curl http://127.0.0.1:8000/health

```

4️⃣ **Test Nginx routing**

```
curl -I http://localhost
curl -I https://stage.omilabs.de

```

5️⃣ **Check Docker compose status**

```
docker compose ps
```

6️⃣ **Rebuild & redeploy locally (for debugging)**

```
docker compose down
docker compose up --build
```

7️⃣ **Debug network issues**

```
sudo ss -tlnp | grep 80
sudo ss -tlnp | grep 443
docker network ls
docker network inspect omilabs_kumo_django_app

```

## 🛡 Security Best Practices

This project already includes:

  * GHCR private images
  * Trivy vulnerability scanning
  * Limited file system mounts
  * Docker networks for isolation
  * TLS/HTTPS enforced
  * No SQL credentials inside image 
  * Secrets stored outside container (/run/kumo/secret_key)

You may add:

  * Fail2ban on server
  * IP allowlists
  * Django SECURE settings
  * Automated SSL renewal systemd timer

📝 Roadmap

Add Prometheus/Grafana monitoring
Add Sentry for error tracking
Enable automated Trivy security gate (block deployments)
Add Blue-Green Deployment
Add staging → production promotion workflow


## 👤 Author

Samuel Omitogun (Omilabs)
Cloud & DevOps Engineer 
Munich, Germany