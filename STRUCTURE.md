# 📁 Project: FastAPI + Next.js Music App

```bash
/fastapi-nextjs-music
├── frontend/                   # 🎨 Frontend application (Next.js)
│   ├── public/                 # 🌄 Static assets (images, icons, etc.)
│   ├── src/
│   │   ├── components/         # 🧩 Reusable UI components
│   │   ├── app/                # 📄 App pages (Next.js App Router)
│   │   ├── store/              # 🗃️ State management (Zustand/Redux)
│   │   └── utils/              # 🛠️ Utility functions and helpers
│   ├── Dockerfile              # 🐳 Dockerfile for frontend
│   ├── package.json            # 📦 NPM dependencies and scripts
│   └── .env                    # 🔐 Environment variables
│
├── backend/   
│   ├── gateway/                    # 🚪 API Gateway (FastAPI)
│   │   ├── app/                    # ⚙️ Core application logic
│   │   ├── routes/                 # 🔀 API routing
│   │   ├── Dockerfile              # 🐳 Dockerfile for API Gateway
│   │   ├── requirements.txt        # 📦 Python dependencies
│   │   └── .env                    # 🔐 Environment variables
│   │
│   ├── user-service/               # 👤 User management service (FastAPI)
│   │   ├── app/                    # ⚙️ Business logic
│   │   ├── models/                 # 📚 Data models (Pydantic/ORM)
│   │   ├── db/                     # 🗄️ Database interaction
│   │   ├── Dockerfile              # 🐳 Dockerfile
│   │   ├── requirements.txt        # 📦 Python dependencies
│   │   └── .env                    # 🔐 Environment variables
│   │
│   ├── track-service/              # 🎵 Music content service (FastAPI)
│   │   ├── app/
│   │   ├── models/
│   │   ├── db/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── .env
│   │
│   ├── playlist-service/           # 📀 Playlist management service (FastAPI)
│   │   ├── app/
│   │   ├── models/
│   │   ├── db/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   └── └── .env
│
├── nginx/                      # 🌐 NGINX for request proxying
│   ├── conf/                   # ⚙️ NGINX configuration files
│   ├── Dockerfile
│   └── default.conf
│
├── rabbitmq/                   # 🐇 RabbitMQ (message broker)
│   ├── Dockerfile
│   └── .env
│
├── postgres/                   # 🐘 PostgreSQL (database)
│   ├── Dockerfile
│   └── .env
│
├── redis/                      # 🧠 Redis (cache)
│   ├── Dockerfile
│   └── .env
│
├── elasticsearch/              # 🔍 Elasticsearch (search engine)
│   ├── Dockerfile
│   └── .env
│
├── docker-compose.yml          # 🧩 Docker Compose configuration
├── README.md                   # 📘 Project documentation
├── .gitignore                  # 🙈 Git ignore file
└── .env                        # 🌍 Global environment variables
