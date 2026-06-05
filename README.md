# AI App Compiler

A Multi-Stage AI App Compiler built using FastAPI.

## Pipeline

1. Intent Extraction
2. System Design
3. Schema Generation
4. Validation
5. Repair

## Supported Applications

- Chat Application
- CRM
- Hospital Management System
- E-Commerce

## API Endpoint

POST /generate

Example Request:

{
  "prompt": "Build a CRM application"
}

## Run

pip install fastapi uvicorn pydantic

python -m uvicorn main:app --reload

Open:
http://127.0.0.1:8000/docs
