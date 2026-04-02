# ☸️ Phase 2: Docker Swarm – Distributed Deployment

## 📌 Overview

This phase demonstrates deploying microservices in a **distributed cluster using Docker Swarm**.

---

## 🏗️ Cluster Architecture

* 3 Manager Nodes
* 2 Worker Nodes
* Hosted on AWS EC2

---

## ⚙️ Features Implemented

* Overlay Networking
* Service Discovery (DNS)
* Load Balancing (Routing Mesh)
* High Availability
* Rolling Updates

---

## 🔧 Initialize Swarm

```bash
docker swarm init --advertise-addr <MANAGER-IP>
```

---

## 🔗 Join Nodes

```bash
docker swarm join --token <TOKEN> <MANAGER-IP>:2377
```

---

## 📦 Build & Push Images

```bash
docker build -t deepagangadhar/account-service:v1 .
docker push deepagangadhar/account-service:v1
```

Repeat for all services.

---

## 🚀 Deploy Stack

```bash
docker stack deploy -c docker-stack.yml bank-app
```

---

## 📊 Verify Services

```bash
docker service ls
docker service ps bank-app_account
```

---

## 🌐 Access Application

```bash
http://<EC2-PUBLIC-IP>:4000/transaction
```

---

## 🔗 Internal Communication

Services communicate using DNS:

```bash
http://account:3000/accounts
```

---

## 🧪 Overlay Network Testing

```bash
docker service create \
  --name test-curl \
  --network bank-app_bank-net \
  curlimages/curl sleep 1000
```

```bash
docker exec -it <container-id> sh
curl http://account:3000/accounts
```

---

## 🔄 Rolling Updates

```yaml
update_config:
  parallelism: 1
  delay: 10s
```

---

## ♻️ Self-Healing

* Containers restart automatically on failure
* Services rescheduled across nodes

---

## 🐞 Challenges & Fixes

### ❌ Service Restart Loop

✔ Fixed incorrect Dockerfile entrypoint

### ❌ DNS Resolution Issue

✔ Verified using overlay network testing

### ❌ Service Communication Failure

✔ Used service names instead of localhost

---

## 🧠 Key Learnings

* Docker Swarm architecture
* Overlay networking
* Distributed system debugging
* Load balancing concepts

---

## 🚀 Future Improvements

* CI/CD integration
* Monitoring (Prometheus, Grafana)
* Kubernetes migration
