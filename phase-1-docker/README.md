# 🐳 Phase 1: Docker – Local Microservices Setup

## 📌 Overview

In this phase, the banking microservices are containerized and run locally using Docker.

---

## 🏗️ Services

* Account Service (Node.js)
* Transaction Service (Flask)
* Notification Service (Node.js)

---

## ⚙️ Prerequisites

* Docker installed

---

## 🔧 Build Images

```bash
docker build -t account-service ./services/account-service
docker build -t transaction-service ./services/transaction-service
docker build -t notification-service ./services/notification-service
```

---

## ▶️ Run Containers

```bash
docker run -d -p 3000:3000 account-service
docker run -d -p 4000:4000 transaction-service
```

---

## 🌐 Access Services

* Account Service:

```bash
http://localhost:3000/accounts
```

* Transaction Service:

```bash
http://localhost:4000/transaction
```

---

## 🔗 Service Communication

Initially, services communicate using:

```bash
http://localhost:<port>
```

---

## 🧠 Learnings

* Containerizing applications
* Managing multiple services locally
* Basic networking between containers

---

## ⚠️ Limitations

* No scalability
* No load balancing
* No fault tolerance

---

## 🚀 Next Step

Move to **Docker Swarm** for distributed deployment.
