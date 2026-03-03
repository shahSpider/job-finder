# Job Finder Platform

An asynchronous job aggregation and matching platform built with FastAPI, PostgreSQL, and SQLAlchemy (async).

This project goes beyond simple CRUD by focusing on structured architecture, service layers, and scalable backend design.

---

## 🚀 Features

- User registration and authentication (JWT ready)
- Job source management
- Job aggregation from multiple sources
- Structured service layer (business logic separated from API layer)
- Async SQLAlchemy with PostgreSQL
- Clean, modular project structure
- Production-ready naming conventions for migrations

---

## 🏗 Project Structure

app/
 ├── main.py
 ├── core/          # Config, security, database engine
 ├── db/            # Base, session, mixins
 ├── models/        # SQLAlchemy models
 ├── schemas/       # Pydantic schemas
 ├── services/      # Business logic layer
 ├── api/           # Route definitions

---

## 🛠 Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy (Async)
- Pydantic
- Passlib (bcrypt)
- Alembic (for migrations)

---

## ⚙️ Setup

### 1. Clone repository

```bash
git clone <repo-url>
cd job-finder# job-finder
