# FastAPI Cheat Sheet

## Part 1: Prerequisites & Must-Know Concepts

### 1. Python Fundamentals
- **Syntax & Data Types:** Integers, floats, booleans, strings, lists, tuples, dictionaries, sets.
- **Control Flow:** `if/else`, `for` loops, `while` loops.
- **Functions:** Parameter passing, return values, scoping.
- **Classes & OOP:** Understanding classes, methods, inheritance, and instances.

### 2. Virtual Environments & Package Management
- **Why Virtual Environments?** Prevents dependency conflicts.
- **Tools:** `venv`, `pipenv`, `conda`.
- **Dependency Management:** Using `pip` or `poetry`.

### 3. HTTP & REST Basics
- **HTTP Methods:** `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
- **HTTP Status Codes:** `200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, `500 Internal Server Error`.
- **REST Concepts:** Resources, endpoints, CRUD operations, statelessness.
- **JSON:** Standard format for request/response bodies.

### 4. Asynchronous Programming (AsyncIO)
- **Synchronous vs. Asynchronous:** Blocking vs. non-blocking I/O.
- **AsyncIO Basics:** `async` and `await` keywords.
- **Event Loop:** Task scheduling and concurrency.

### 5. Modern Python Tooling & Typing
- **Type Hints:** `def my_function(name: str) -> int:`
- **Static Type Checkers:** `mypy`, `pyright`.
- **Linters & Formatters:** `flake8`, `black`, `isort`.

### 6. Basic SQL & Databases (Optional but Helpful)
- **Database Fundamentals:** Tables, columns, primary/foreign keys.
- **CRUD in SQL:** `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- **ORM Concepts:** Using `SQLAlchemy`, `Peewee`, etc.

### 7. Basic HTML & Front-End Interaction (Optional but Helpful)
- Understanding API consumption from the client-side perspective.

---

## Part 2: FastAPI Roadmap — Beginner to Advanced

### Beginner Level

#### Project Setup
**Install FastAPI:**
```bash
pip install fastapi uvicorn
```
**Minimal Hello World:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}
```
**Run the Server:**
```bash
uvicorn main:app --reload
```

#### Basic Routing & Path Parameters
```python
@app.get("/items")
def get_items():
    return ["item1", "item2", "item3"]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}
```

#### Query Parameters & Request Body
```python
@app.get("/search")
def search_items(q: str = None):
    return {"results": f"Results for query: {q}"}
```
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return {"msg": "Item created", "item": item.dict()}
```

#### Automatic Docs
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

**Key Focus:**
- Define endpoints (`@app.get`, `@app.post`, etc.).
- Request data handling (`Path`, `Query`, `Body`).
- Explore documentation features.

---

### Intermediate Level

#### Advanced Pydantic Models
**Nested Models:**
```python
class User(BaseModel):
    username: str
    email: str

class Post(BaseModel):
    title: str
    content: str
    author: User
```
**Custom Validations:**
```python
from pydantic import validator

class Item(BaseModel):
    name: str
    price: float

    @validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be positive')
        return value
```

#### Path Operations Configuration
```python
@app.get("/users/{user_id}", tags=["User Operations"], response_model=User)
def read_user(user_id: int):
    """
    Fetch a user by their ID.
    """
    ...
```

#### Dependency Injection
```python
from fastapi import Depends

def get_db():
    db = SomeDBConnection()
    try:
        yield db
    finally:
        db.close()

@app.get("/items")
def read_items(db=Depends(get_db)):
    return db.get_items()
```

#### Middleware & Hooks
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### Database Integration
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
```

**Key Focus:**
- Master `pydantic` validation.
- Integrate a database.
- Implement authentication & authorization.

---

### Advanced Level

#### Scaling & Deployment
- **Production Servers:** `gunicorn`, `hypercorn` with `uvicorn` workers.
- **Containers:** Dockerize FastAPI apps.
- **CI/CD Pipelines:** GitHub Actions, GitLab CI.

#### Async Performance & Concurrency
```python
from fastapi import BackgroundTasks

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message)

@app.post("/log")
def create_log(background_tasks: BackgroundTasks, message: str):
    background_tasks.add_task(write_log, message)
    return {"message": "Log creation in background"}
```

#### WebSockets & Real-Time Communication
```python
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")
```

**Key Focus:**
- Secure, scalable applications.
- CI/CD, containers, and orchestration tools.
- WebSockets and real-time communication.
- Performance optimization.

---

## Summary
1. **Start with strong Python fundamentals** (async/await, HTTP/REST, databases).
2. **Beginner:** Learn FastAPI basics (routing, Pydantic models, documentation).
3. **Intermediate:** Advanced Pydantic features, authentication, middleware, DB integration.
4. **Advanced:** Secure, scalable applications with microservices, WebSockets, and CI/CD.

Master these concepts to build robust FastAPI applications!

