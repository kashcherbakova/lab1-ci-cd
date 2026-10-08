# Lab 1 - CI/CD REST API

## Description

This project is a basic REST API developed for Laboratory Work #1.

The application implements CRUD operations for items.

## Technologies

- Python 3.13
- FastAPI
- Uvicorn
- Pytest
- Docker
- GitHub
- Azure DevOps
- Docker Hub

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /api/items | Get all items |
| GET | /api/items/{id} | Get item by ID |
| POST | /api/items | Create item |
| PUT | /api/items/{id} | Update item |
| DELETE | /api/items/{id} | Delete item |

## Run locally

## Install dependencies:

bash
pip install -r requirements.txt

## Run application:
uvicorn app.main:app --reload

## Swagger UI:
http://127.0.0.1:8000/docs

## Run tests
pytest -q

## Build Docker image
docker build -t lab1-fastapi .

## Run Docker container
docker run -d -p 8000:8000 --name lab1-fastapi-container lab1-fastapi

## Swagger UI:
http://localhost:8000/docs