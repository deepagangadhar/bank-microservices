# 🚀 Bank Microservices Platform

This project demonstrates a **microservices-based banking system** built and deployed using:

* **Docker (Phase 1)** – Local containerized setup
* **Docker Swarm (Phase 2)** – Distributed cluster on AWS

---

## 🧩 Project Evolution

### 🔹 Phase 1: Docker (Local Development)

* Containerized services
* Local networking
* Manual container management

### 🔹 Phase 2: Docker Swarm (Production-Style Deployment)

* Multi-node cluster (3 Managers + 2 Workers)
* Overlay networking
* Load balancing (Routing Mesh)
* Self-healing containers
* Rolling updates

---

## 🏗️ Services

| Service              | Tech    | Description              |
| -------------------- | ------- | ------------------------ |
| Account Service      | Node.js | Provides account details |
| Transaction Service  | Flask   | Processes transactions   |
| Notification Service | Node.js | Sends notifications      |

---

## 📂 Project Structure

```
bank-microservices/
│
├── phase-1-docker/
├── phase-2-swarm/
├── services/
│   ├── account-service/
│   ├── transaction-service/
│   └── notification-service/
```

---

## 📘 Documentation

* 🔹 [Phase 1: Docker Setup](./phase-1-docker/README.md)
* 🔹 [Phase 2: Docker Swarm Deployment](./phase-2-swarm/README.md)

---

## 🌐 Key Concepts Demonstrated

* Microservices Architecture
* Containerization
* Service Discovery
* Overlay Networking
* Load Balancing
* High Availability

---

## 👨‍💻 Author

Deepa Gangadhar

---

⭐ If you like this project, give it a star!
