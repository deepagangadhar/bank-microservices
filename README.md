# 🏦 Bank Microservices Deployment using Docker & AWS

## 📌 Overview

This project demonstrates a simple **microservices architecture** deployed using **Docker containers on AWS EC2**.

The system consists of three services:

* Account Service (Node.js)** – Provides account details
* Transaction Service (Flask)** – Orchestrates transactions
* Notification Service (Flask)** – Sends notifications

---

## 🧩 Architecture

Client → Transaction Service → Account Service
→ Notification Service

---

## ⚙️ Tech Stack

* Node.js (Express)
* Python (Flask)
* Docker
* AWS EC2
* REST APIs

---

## 🚀 Features

* Containerized microservices using Docker
* Service-to-service communication using Docker networking
* External access via port mapping
* Deployed on AWS EC2
* Simple API orchestration across services

---

## 📁 Project Structure

```
bank-microservices/
│
├── account/
├── transaction/
├── notification/
└── docker-compose.yml
```

---

## 🐳 Running Locally

```bash
docker-compose up --build
```

---

## 🌐 API Endpoints

| Service      | Endpoint     |
| ------------ | ------------ |
| Account      | /accounts    |
| Notification | /notify      |
| Transaction  | /transaction |

---

## ☁️ Deployment on AWS

1. Launch EC2 instance (Ubuntu)
2. Install Docker & Docker Compose
3. Clone repository
4. Run:

```bash
docker-compose up --build -d
```

5. Access:

```
http://<EC2-IP>:4000/transaction
```

---

## 🔍 Key Learnings

* Docker containerization
* Microservices communication
* Port mapping and networking
* Cloud deployment on AWS
* Debugging container issues

---

## 📌 Future Improvements

* Add NGINX API Gateway
* Implement CI/CD pipeline
* Migrate to Kubernetes

---

## 👩‍💻 Author

Deepa Gangadhar

