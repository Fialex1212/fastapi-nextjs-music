# 🎧 Project Tech Stack (MVP)

## 🖥️ Frontend

| Component            | Technology                         |
|----------------------|------------------------------------|
| Framework            | Next.js (with SSR/ISR)             |
| Styling              | Tailwind CSS                       |
| State Management     | Zustand                            |
| Audio Player         | Wavesurfer.js                      |
| Authentication       | OAuth2 (HttpOnly cookie)           |
| SEO / SSR            | Yes                                |

---

## 🛠️ Backend (Microservices)

| Service             | Technologies                            |
|---------------------|-----------------------------------------|
| API Gateway         | FastAPI                                 |
| Auth                | FastAPI                                 |
| User Service        | FastAPI                                 |
| Music Service       | FastAPI                                 |
| Playlist Service    | FastAPI                                 |
| Streaming Proxy     | NGINX                                   |
| Analytics           | Kafka + ClickHouse / PostgreSQL         |
| Search              | Elasticsearch                           |

---

## 💾 Storage

| Purpose             | Technology                           |
|---------------------|--------------------------------------|
| Main DB             | PostgreSQL                           |
| Cache               | Redis                                |
| Search              | Elasticsearch                        |
| Audio Storage       | MinIO / Amazon S3                    |

---

## 🔐 Authentication

| Purpose             | Technology                           |
|---------------------|--------------------------------------|
| OAuth2 Provider     | Keycloak or Custom Service           |
| Authorization       | JWT                                  |
| Refresh Tokens      | Redis                                |
| SSO Support         | Google OAuth2                        |

---

## ⚙️ DevOps

| Purpose             | Technology                           |
|---------------------|--------------------------------------|
| Containerization    | Docker + Docker Compose              |
| CI/CD               | GitHub Actions                       |
| Orchestration       | Kubernetes                           |
| Monitoring          | Prometheus + Grafana                 |
| Logging             | Loki                                 |
| Tracing             | Jaeger                               |
| Message Broker      | RabbitMQ                             |

---

## 📦 Additional Services

| Purpose             | Tool                                  |
|---------------------|---------------------------------------|
| Email/SMS           | SendGrid / Mailgun / Twilio           |
| Payments            | Stripe / CloudPayments                |
| Documentation       | Swagger                               |
| Visualization       | tldraw                                |