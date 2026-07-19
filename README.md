# 📝 TaskFlow - Flask To-Do Application

TaskFlow is a modern task management web application built using **Flask**, **SQLAlchemy**, and **SQLite**. It allows users to register, log in securely, and manage their personal tasks with an intuitive and responsive interface.

---

## 🚀 Features

- 🔐 User Registration
- 🔑 Secure Login System
- 👤 User-specific task management
- ➕ Add new tasks
- 🔄 Update task status (Pending → Working → Done)
- 🗑️ Clear all personal tasks
- 💾 SQLite database integration
- 📱 Responsive and modern UI
- 💬 Flash messages for user feedback

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Jinja2 Templates

### Backend
- Flask
- Flask-SQLAlchemy
- Werkzeug Security

### Database
- SQLite

---

## 📂 Project Structure

```
TaskFlow/
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   └── tasks.py
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── tasks.html
│   │
│   ├── models.py
│   └── __init__.py
│
├── instance/
│   └── todo.db
│
├── create_db.py
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/taskflow.git
```

```bash
cd taskflow
```

---

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install flask
pip install flask_sqlalchemy
```

or

```bash
pip install -r requirements.txt
```

---

### 4. Create the Database

```bash
python create_db.py
```

---

### 5. Run the Application

```bash
python run.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Application Workflow

1. Register a new account.
2. Login using your credentials.
3. Add new tasks.
4. Change task status:
   - Pending
   - Working
   - Done
5. Clear all your tasks when required.
6. Logout securely.

---

## 🗄️ Database Schema

### User

| Field | Type |
|-------|------|
| id | Integer |
| username | String |
| password | String (Hashed) |

### Task

| Field | Type |
|-------|------|
| id | Integer |
| title | String |
| status | String |
| user_id | Foreign Key |

---

## 🔒 Authentication

The application uses:

- Flask Sessions
- Password Hashing with Werkzeug
- User-specific task access
- Protected routes

Each user can only view and manage their own tasks.

---

## 🎨 User Interface

The application includes:

- Responsive layout
- Modern navigation bar
- Card-based task dashboard
- Status badges
- Animated buttons
- Clean login and registration pages
- Flash notifications

---

## 📌 Future Improvements

- Task deletion
- Task editing
- Due dates
- Priority levels
- Task categories
- Search and filters
- Profile page
- Dark mode
- Email verification
- Password reset
- REST API
- Docker deployment

---

## 📄 License

This project is developed for educational purposes and can be modified or extended for personal and academic use.

---

## 👨‍💻 Author

**Vaibhav Barnwal**

B.Tech – Computer Science & Engineering (AI & ML)

Email: **vaib07052@gmail.com**

GitHub: **https://github.com/vaib07052**