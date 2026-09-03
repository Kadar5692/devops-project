# 🚀 DevOps Project — Flask Application

A containerized Flask web application demonstrating a complete **CI/CD DevOps workflow** using GitHub, GitHub Actions, Docker, Docker Hub, and Render.

## 🌐 Live Application

**Live Website:**
https://devops-project-ovnk.onrender.com/

---

## 📌 Project Overview

This project demonstrates how a simple Flask application can be developed, tested, containerized, and automatically deployed to the cloud using modern DevOps practices.

The application is packaged using Docker and integrated with a CI/CD pipeline. Whenever new code is pushed to the `main` branch, automated testing and Docker image building are performed, followed by automatic deployment to Render.

---

## 🏗️ DevOps Workflow

```text
                 👨‍💻 Developer
                      │
                      ▼
                  VS Code
                      │
                  Git Commit
                      │
                      ▼
                    GitHub
                      │
                  Git Push
                      │
                      ▼
             ┌─────────────────┐
             │ GitHub Actions  │
             │                 │
             │ • Test Flask    │
             │ • Build Docker  │
             └────────┬────────┘
                      │
                      ▼
                Docker Hub
                      │
                      │
                      ▼
                  🐳 Docker
                      │
                      ▼
                  ☁️ Render
                      │
                      ▼
              🌐 Live Website
```

---

## 🛠️ Technologies Used

| Technology         | Purpose                             |
| ------------------ | ----------------------------------- |
| **Python**         | Application programming language    |
| **Flask**          | Web application framework           |
| **Git**            | Version control                     |
| **GitHub**         | Source code repository              |
| **GitHub Actions** | Continuous Integration / automation |
| **Docker**         | Application containerization        |
| **Docker Hub**     | Docker image registry               |
| **Render**         | Cloud deployment and hosting        |

---

## 📂 Project Structure

```text
devops-project/
│
├── app/
│   └── app.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🐍 Flask Application

The application is built using Flask and listens on the port provided by the deployment environment.

```python
app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000))
)
```

Using the `PORT` environment variable allows the application to work both locally and on cloud platforms such as Render.

---

## 🐳 Docker

The application is containerized using Docker.

### Build the Docker image

```bash
docker build -t devops-project .
```

### Run the container

```bash
docker run -p 5000:5000 --name devops-container devops-project
```

The application can then be accessed locally at:

```text
http://localhost:5000
```

---

## 🔄 CI/CD Pipeline

GitHub Actions is used to automate the project's Continuous Integration process.

The pipeline:

1. Checks out the source code.
2. Sets up Python.
3. Installs project dependencies.
4. Tests the Flask application.
5. Builds the Docker image.
6. Pushes the Docker image to Docker Hub.

### Pipeline Trigger

The workflow runs when code is pushed to the `main` branch or when a pull request targets `main`.

---

## 🐳 Docker Hub

The Docker image is published to Docker Hub using the `latest` tag.

```text
kadar786/devops-project:latest
```

Docker Hub provides a centralized location for storing and distributing the container image.

---

## ☁️ Cloud Deployment

The application is deployed on **Render** using the GitHub repository and Dockerfile.

### Automatic Deployment

The project is configured for automatic deployment.

```text
Code Change
     ↓
Git Push
     ↓
GitHub
     ↓
GitHub Actions
     ↓
Render Auto-Deploy
     ↓
Updated Live Application
```

An automatic deployment test was successfully completed using commit:

```text
ff6cf37
```

The Render deployment was triggered automatically and completed successfully.

---

## 🧪 Testing

The Flask application can be tested locally using:

```bash
python -c "from app.app import app; print('Flask test passed')"
```

Expected output:

```text
Flask test passed
```

---

## 🔐 Environment Variables

The application uses the following environment variable when deployed:

```text
PORT
```

The application automatically uses the platform-provided port and falls back to port `5000` when running locally.

---

## 🎯 Key DevOps Concepts Demonstrated

* Version Control
* Source Code Management
* Continuous Integration
* Automated Testing
* Containerization
* Docker Image Management
* CI/CD Automation
* Cloud Deployment
* Automatic Deployment
* Environment-based Configuration

---

## 🚀 Future Improvements

The project can be extended with additional DevOps technologies and practices:

* **AWS** — cloud infrastructure
* **Terraform** — Infrastructure as Code
* **Ansible** — server configuration automation
* **Jenkins** — alternative CI/CD platform
* **Nginx** — reverse proxy and web server
* HTTPS/SSL configuration
* Application monitoring
* Logging and health checks
* Automated security scanning

---

## 👨‍💻 Author

**Kadar Alli Sha**

MBA Finance | 2024–2026
CDOE, Utkal University

---

## 📄 License

This project is created for educational and learning purposes.
