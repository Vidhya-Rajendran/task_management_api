# 🚀 Task Management API

A backend application built using **FastAPI** to manage tasks with full CRUD functionality.
This project demonstrates a clean and scalable backend architecture using routers, services, and database layers, along with async database operations.

---

## ✨ Features

* Create, Read, Update, Delete (CRUD) operations for tasks
* Request validation using Pydantic
* Async database operations with SQLAlchemy
* PostgreSQL database integration
* Dockerized setup using Docker Compose
* Interactive API documentation with Swagger UI
* Clean layered architecture (Router → Service → Database)

---
## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy (Async)
* **Validation:** Pydantic
* **Containerization:** Docker & Docker Compose

---

## 🐳 Running with Docker

### 1. Clone the repository

```
git clone https://github.com/Vidhya-Rajendran/task_management_api.git
cd task_management_api
```

---

### 2. Start the application

```
docker compose up --build
```

---

### 3. Access the application

* API Base URL: http://localhost:8080
* Swagger UI: http://localhost:8080/docs

---

## 📡 API Endpoints

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| POST   | /tasks      | Create a task  |
| GET    | /tasks      | Get all tasks  |
| GET    | /tasks/{id} | Get task by ID |
| PUT    | /tasks/{id} | Update task    |
| DELETE | /tasks/{id} | Delete task    |

---

## 🧪 Example Request

### ➕ Create Task

```
POST /tasks
```
Request

```
{
  "title": "Learn FastAPI",
  "description": "Practice CRUD operations"
}
```

Response

```
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Practice CRUD operations",
  "is_completed": false
}
```

### 📥 Get All Tasks
```
GET /tasks
```

Response
```
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Practice CRUD operations",
    "is_completed": false
  }
]
```

### 🔍 Get Task by ID
```
GET /tasks/{task_id}
```

Example
```
GET /tasks/1
```

Response

```
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Practice CRUD operations",
  "is_completed": false
}
```

### ✏️ Update Task
```
PUT /tasks/{task_id}
```

Example
```
PUT /tasks/1
```

Request Body
```
{
  "title": "Learn FastAPI deeply",
  "description": "Practice async SQLAlchemy",
  "is_completed": true
}
```

Response
```
{
  "id": 1,
  "title": "Learn FastAPI deeply",
  "description": "Practice async SQLAlchemy",
  "is_completed": true
}
```

### ❌ Delete Task
```
DELETE /tasks/{task_id}
```

Example
```
DELETE /tasks/1
```

Response
```
204 No Content
```
