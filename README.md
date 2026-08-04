# 🚀 Django_React

A full-stack web application powered by a **Django** backend and a **React** frontend — a clean, decoupled architecture where Django Rest Framework serves the API and React handles the UI.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Backend-092E20?style=flat&logo=django&logoColor=white)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=flat&logo=react&logoColor=black)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 📖 Overview

This project separates concerns cleanly into two parts:

- **`backend/`** — A Django application exposing a REST API (via Django Rest Framework) that handles business logic, data, and authentication.
- **`frontend/`** — A React single-page application that consumes the API and renders the user interface.

This structure makes it easy to develop, test, and deploy the frontend and backend independently.

---

## 🗂️ Project Structure

```
Django_React/
├── backend/          # Django project & apps (API, models, serializers, views)
├── frontend/          # React application (components, pages, assets)
└── README.md
```

---

## ✨ Features

- 🔗 Decoupled architecture — Django REST API + React SPA
- ⚡ Fast local development with hot-reloading on the frontend
- 🔐 Ready to extend with authentication, permissions, and custom endpoints
- 📦 Simple, standard tooling — `pip` for backend, `npm`/`yarn` for frontend



---

## 🛠️ Tech Stack

| Layer      | Technology                     |
|------------|---------------------------------|
| Backend    | Django, Django Rest Framework  |
| Frontend   | React, JavaScript, CSS, HTML   |
| API Format | JSON over REST                 |

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+ and npm (or yarn)
- pip / virtualenv

### 1. Clone the repository

```bash
git clone https://github.com/makarandbhosale0/Django_React.git
cd Django_React
```

### 2. Backend Setup (Django)

```bash
cd backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

The backend will be available at `http://127.0.0.1:8000/`.

### 3. Frontend Setup (React)

Open a new terminal window:

```bash
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will be available at `http://localhost:3000/`.

---

## 🚦 Usage

1. Start the Django backend server.
2. Start the React frontend server.
3. Open your browser at `http://localhost:3000/` — the React app will communicate with the Django API running on port `8000`.

> ⚠️ If you run into CORS issues, make sure `django-cors-headers` is installed and configured in your Django settings to allow requests from `http://localhost:3000`.

---

## 📌 Roadmap

- [ ] Add authentication (JWT / session-based)
- [ ] Add unit & integration tests
- [ ] Add Docker support for one-command setup
- [ ] Deploy to production (e.g. Render, Railway, Vercel)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source. Add your preferred license (e.g. [MIT](https://choosealicense.com/licenses/mit/)) here.

---

## 👤 Author

**Makarand Bhosale**
GitHub: [@makarandbhosale0](https://github.com/makarandbhosale0)

---

<p align="center">Made with ❤️ using Django & React</p>
